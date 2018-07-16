"""
Web module for the PyCompendium app.
"""
from flask import Flask
APP = Flask(__name__)


@APP.route("/")
def index():
    return "PyCompendium IBIS Tool"

