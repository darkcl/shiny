
from flask import Flask

def start_web():
    """Start Web Server"""

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    return app
