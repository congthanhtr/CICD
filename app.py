"""
This is a flask application that serves a simple "Hello World!" page.

The application is defined using the Flask class from the flask module.
The route '/' is defined to return the string "Hello World!"
When the application is run, it listens on port 8090 by default.

"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """
    This function returns a string with the text "Hello World!"
    """
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=8090)