#!/usr/bin/env python3
"""Reduce 1."""
import math
import sys
import itertools


with open("total_document_count.txt") as file:
    N = int(file.read())


def reduce_one_group(key, group):
    """Reduce one group."""
    docs = []
    last_id = -1
    curr_count = 0
    for line in group:
        doc_id = line.split()[1]
        if doc_id == last_id:
            curr_count += 1
        else:
            if last_id != -1:
                docs.extend((last_id, str(curr_count)))
            last_id = doc_id
            curr_count = 1
    if last_id != -1:
        docs.extend((last_id, str(curr_count)))
    num_docs = len(docs) / 2
    idf = math.log10(N / num_docs)
    print(key, idf, " ".join(docs))


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.split()[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
