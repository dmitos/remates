from flask import Blueprint, render_template, request, redirect, flash
from db import mysql


views_clientes = Blueprint(__name__, "views_clientes")


@views_clientes.route("/Clientes")
def cliente():
    base_datos = mysql.get_db()
    cursor = base_datos.cursor()
    cursor.execute('SELECT * FROM Clientes')
    clientes = cursor.fetchall()
    print(clientes)
    return render_template("Clientes/clientes.html", clientes=clientes) 
    # return render_template("Clientes/clientes.html")

@views_clientes.route("/Insertar_Clientes", methods=['POST'])
def insertar_cliente():
    base_datos = mysql.get_db()
    cursor = base_datos.cursor()
    documento = request.form['documento']
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    dpto = request.form['departamento']
    mail = request.form['mail']
    cursor.execute('INSERT INTO Clientes(ClienteDoc, ClienteNombre, ClienteMail, ClienteTelefono, ClienteDireccion, ClienteDepto) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")' % (documento, nombre, mail, telefono, direccion, dpto))
    base_datos.commit()
    print(documento, nombre, mail, telefono, direccion, dpto)
    return redirect("/Clientes")


@views_clientes.route("/Alta_Clientes")
def Alta_Cliente():
    return render_template("Clientes/alta_cliente.html")


@views_clientes.route("/Baja_Cliente/<id>/")
def Baja_Cliente(id):
    base_datos = mysql.get_db()
    cursor = base_datos.cursor()
    cursor.execute('SELECT * FROM Clientes WHERE ClienteId = %s', (id))
    Cliente = cursor.fetchall()
    print(cliente)
    return render_template("Clientes/baja_cliente.html", cliente=Cliente)


@views_clientes.route("/Borrar_Cliente", methods=['post'])
def Borrar_cliente():
    base_datos = mysql.get_db()
    cursor = base_datos.cursor()
    borrar = request.form['id']
    print("se borro cliente", (borrar))
    cursor.execute('DELETE FROM Clientes WHERE ClienteId = %s', (borrar))
    base_datos.commit()
    flash('Se borro el cliente')
    return redirect("/Clientes")


@views_clientes.route("/Perfil_Cliente")
def Perfil_Cliente():
    return render_template("Clientes/perfil_cliente.html")
