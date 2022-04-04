"""Insta485 package initializer."""
import os
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name
app.config["INDEX_PATH"] = os.getenv("INDEX_PATH", "inverted_index_1.txt")

# Overlay settings read from a Python file whose path is set in the environment
# variable INSTA485_SETTINGS. Setting this environment variable is optional.
# Docs: http://flask.pocoo.org/docs/latest/config/
#
# EXAMPLE:
# $ export INSTA485_SETTINGS=secret_key_config.py
app.config.from_envvar('INDEX_SETTINGS', silent=True)

# Tell our app about views and model.  This is dangerously close to a
# circular import, which is naughty, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/patterns/packages/)  We're
# going to tell pylint and pycodestyle to ignore this coding style violation.
import index.api  # noqa: E402  pylint: disable=wrong-import-position
