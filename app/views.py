from flask import render_template, jsonify, request

from app import application
from . import articles


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/about")
def about():
    return render_template("about.html")


@application.route("/api")
def api_root():
    return jsonify({"v1": f"{request.base_url}/v1"})


@application.route("/api/v1")
def api_version_one():
    return jsonify({"articles": f"{request.base_url}/articles"})


@application.route("/api/v1/articles")
def api_v1_fetch_articles_collection():
    return jsonify({"articles": articles.articles_collection})
