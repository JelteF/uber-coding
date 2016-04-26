"""Main module to run the webserver."""

from flask import Flask, render_template, jsonify, url_for, redirect, request
from flask_jsglue import JSGlue

app = Flask(__name__)
JSGlue(app)

app.config.from_object('config.Config')
config = app.config

# Jinja initialization to use PyJade
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

from app.routes import *  # noqa
