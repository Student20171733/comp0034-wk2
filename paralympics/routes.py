from flask import current_app as app
from markupsafe import escape

@app.route('/')
def hello():
  return f"Hello!"

@app.route("/<name>")
def hello_name(name=None):
    return f"Hello, {escape(name)}!"
