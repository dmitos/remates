from flask import Blueprint, render_template, request, redirect


index = Blueprint(__name__, "index")


@index.route("/")
def home():
    return render_template("index.html")
