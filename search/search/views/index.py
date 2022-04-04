"""
Search index (main) view.

URLs include:
/
"""
import flask
import search


@search.app.route('/')
def show_index():
    """Display / route."""
    query = flask.request.args.get('q')
    weight = flask.request.args.get('w')
    context = {
        "show_search": True,
        "search_results": [],
    }
    if query is None or weight is None:
        context["show_search"] = False
    return flask.render_template("index.html", **context)
