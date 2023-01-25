from flask import Blueprint, render_template, request, redirect
# import sqlite3
from db import mysql


views_clientes = Blueprint(__name__, "views_clientes")


@views_clientes.route("/Clientes")
def cliente():
    cursor = mysql.get_db().cursor()
    # db = sqlite3.connect('database.db')
    # cursor = db.cursor()
    cursor.execute('SELECT * FROM Clientes')
    clientes = cursor.fetchall()
    # db.close()
    print(clientes)
    return render_template("Clientes/clientes.html", clientes=clientes)


@views_clientes.route("/Insertar_Clientes", methods=['post'])
def insertar_cliente():
    #db = sqlite3.connect('database.db')
    #cursor = db.cursor()
    #nombre = request.form['nombre']
    #direccion = request.form['direccion']
    #telefono = request.form['telefono']
    #mail = request.form['mail']
    #cursor.execute('INSERT INTO clientes(nombre, direccion, telefono, mail) VALUES("%s", "%s", "%s", "%s")' % (nombre, direccion, telefono, mail))
    #db.commit()
    #db.close()
    return redirect("/Clientes")


@views_clientes.route("/Agregar_Clientes")
def agregar_cliente():
    return render_template("Clientes/agregar_cliente.html")
