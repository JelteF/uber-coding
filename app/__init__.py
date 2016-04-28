"""Main module to run the webserver."""

from flask import Flask, render_template, jsonify, url_for, redirect, request
from flask_jsglue import JSGlue

app = Flask(__name__)
JSGlue(app)

try:
    app.config.from_object('config.Config')
except:
    app.config.from_object('default_config.DefaultConfig')
config = app.config

# Jinja initialization to use PyJade
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

from app.routes import *  # noqa
