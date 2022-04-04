"""index api."""
import math
import pathlib
import re

import flask

import index


@index.app.before_first_request
def startup():
    """Load inverted index, pagerank, and stopwords into memory."""
    index_dir = pathlib.Path(__file__).parent.parent
    read_stopwords(index_dir)
    read_pagerank(index_dir)
    read_inverted_index(index_dir)


@index.app.route('/api/v1/')
def service_list():
    """Show service list."""
    context = {
        "hits": "/api/v1/hits/",
        "url": "/api/v1/",
    }
    return flask.jsonify(**context)


@index.app.route('/api/v1/hits/')
def hits():
    """Show a list of hits from query."""
    query = flask.request.args.get('q')
    weight = float(flask.request.args.get('w', default=0.5))
    query = clean_query(query)
    results = search(query, weight)
    context = {
        "hits": results,
    }
    return flask.jsonify(**context)


def read_stopwords(index_dir):
    """Load stopwords into memory."""
    index.stopwords = set()
    with open(index_dir / 'stopwords.txt', 'r', encoding="utf-8") as file:
        for line in file:
            index.stopwords.add(line.strip())


def read_pagerank(index_dir):
    """Load pagerank into memory."""
    index.pagerank = {}
    with open(index_dir / 'pagerank.out', 'r', encoding="utf-8") as file:
        for line in file:
            doc_id, rank = line.strip().split(',')
            index.pagerank[doc_id] = float(rank)


def read_inverted_index(index_dir):
    """Load inverted index into memory."""
    index.inverted_index = {}
    inverted_index_file = (
            index_dir / 'inverted_index' / index.app.config["INDEX_PATH"]
    )
    with open(inverted_index_file, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.split()
            term = line[0]
            idf = line[1]
            num_docs = (len(line) - 2) // 3
            index.inverted_index[term] = {}
            index.inverted_index[term]["idf"] = float(idf)
            index.inverted_index[term]["docs"] = {}
            for i in range(num_docs):
                doc_id = line[3 * i + 2]
                term_frequency = line[3 * i + 3]
                norm_factor = line[3 * i + 4]
                index.inverted_index[term]["docs"][doc_id] = {
                    "tf": term_frequency,
                    "norm_factor": norm_factor,
                }


def clean_query(query):
    """Clean query."""
    query = re.sub(r"[^a-zA-Z0-9 ]+", "", query)
    query = query.casefold()
    query = query.split()
    query = [word for word in query if word not in index.stopwords]
    result = {}
    for term in query:
        if term in result:
            result[term] += 1
        else:
            result[term] = 1
    return result


def search(query, weight):
    """Search for query."""
    # Calculate query vector
    pterm = list(query.keys())[0]
    doc_ids = set(index.inverted_index[pterm]["docs"].keys())
    # Get all documents that contain all the terms in query
    for term in query:
        if term not in index.inverted_index:
            return []
        doc_ids = doc_ids.intersection(
            set(index.inverted_index[term]["docs"].keys())
        )
    # Calculate score for each document
    results = []
    for doc_id in doc_ids:
        query_vector = []
        document_vector = []
        norm_d_squared = 0
        for term in query:
            # Calculate query vector
            term_frequency = query[term]
            idf = index.inverted_index[term]["idf"]
            query_vector.append(term_frequency * idf)
            # Calculate document vector
            term_frequency = int(
                index.inverted_index[term]["docs"][doc_id]["tf"]
            )
            idf = index.inverted_index[term]["idf"]
            document_vector.append(term_frequency * idf)
            # Calculate norm_d_squared
            norm_d_squared = (
                index.inverted_index[term]["docs"][doc_id]["norm_factor"]
            )
        # Calculate cosine similarity
        tfidf = sum([x * y for x, y in zip(query_vector, document_vector)]) / \
            (math.sqrt(sum([x * x for x in query_vector])) *
             math.sqrt(float(norm_d_squared)))
        pagerank = index.pagerank[doc_id]
        weighted_score = weight * pagerank + (1 - weight) * tfidf
        results.append({
            "docid": int(doc_id),
            "score": weighted_score,
        })
    # Sort by score
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
