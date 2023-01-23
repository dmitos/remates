from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3


from view_clientes import views_clientes
from index import index

app = Flask(__name__)
app.register_blueprint(views_clientes, url_prefix="/")
app.register_blueprint(index, url_prefix="/")
con=sqlite3.connect("database.db")
con.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY, nombre TEXT, direccion TEXT, telefono INTEGER, mail TEXT)")
con.close()

if __name__ == '__main__':
    app.run(debug=True)
