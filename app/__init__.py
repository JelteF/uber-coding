"""Main module to run the webserver."""

from flask import Flask
from flask_jsglue import JSGlue

app = Flask(__name__)
JSGlue(app)

app.config.from_object('config.Config')
