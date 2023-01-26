from flask import Flask, render_template, request, flash, redirect, url_for
# import sqlite3
from db import mysql


from view_clientes import views_clientes
from index import index

app = Flask(__name__)
app.register_blueprint(views_clientes, url_prefix="/")
app.register_blueprint(index, url_prefix="/")
#app.config['MYSQL_DATABASE_HOST'] = 'sql10.freesqldatabase.com'
#app.config['MYSQL_DATABASE_PORT'] = 3306
#app.config['MYSQL_DATABASE_USER'] = 'sql10593302'
#app.config['MYSQL_DATABASE_PASSWORD'] = '5UrY7aPKIR'
#app.config['MYSQL_DATABASE_DB'] = 'sql10593302'

# app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
# app.config['MYSQL_DATABASE_PORT'] = 3306
# app.config['MYSQL_DATABASE_USER'] = 'sqremates'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'dana1916'
# app.config['MYSQL_DATABASE_DB'] = 'sqremates'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dana'
app.config['MYSQL_DATABASE_DB'] = 'prueba'
mysql.init_app(app)
# con = sqlite3.connect("database.db")
# con.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY, nombre TEXT, direccion TEXT, telefono INTEGER, mail TEXT)")
# con.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
