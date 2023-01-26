from flask import Blueprint, render_template, request, redirect
# from db import mysql


views_clientes = Blueprint(__name__, "views_clientes")


@views_clientes.route("/Clientes")
def cliente():
    # cursor = mysql.get_db().cursor()
    # cursor.execute('SELECT * FROM Clientes')
    # clientes = cursor.fetchall()
    # print(clientes)
    # return render_template("Clientes/clientes.html", clientes=clientes) cuando este la base de datos
    return render_template("Clientes/clientes.html")

@views_clientes.route("/Insertar_Clientes", methods=['post'])
def insertar_cliente():
    # cursor = mysql.get_db().cursor()
    # nombre = request.form['nombre']
    # direccion = request.form['direccion']
    # telefono = request.form['telefono']
    # mail = request.form['mail']
    # cursor.execute('INSERT INTO Clientes(nombre, telefono, direccion) VALUES("%s", "%s", "%s")' % (nombre, telefono, direccion))
    return redirect("/Clientes")


@views_clientes.route("/Agregar_Clientes")
def agregar_cliente():
    return render_template("Clientes/agregar_cliente.html")
