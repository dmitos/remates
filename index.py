from flask import Blueprint, render_template, request, redirect
import sqlite3

index = Blueprint(__name__, "index")

@index.route("/")
def home():
    return render_template("index.html")