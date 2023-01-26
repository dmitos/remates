from flask import Blueprint, render_template


# genero el enlazador de blueprint
index = Blueprint(__name__, "index")

@index.route("/")
def home():
    return render_template("index.html")
