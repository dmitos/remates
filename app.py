# importamos flask
from flask import Flask

'''
cuando tenga la base hay q
descomentar el from db import mysql

'''
from db import mysql

# Agrego los blueprint()
from views_clientes import views_clientes  # importo el manejador de clientes
from index import index  # importo el manejador del inicio 

# inicio la clase Flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# registro los blueprint antes importados y le doy direccion de prefijo
app.register_blueprint(views_clientes, url_prefix="/")
app.register_blueprint(index, url_prefix="/")

'''
Descomentar la base de datos que voy a usar en su momento

'''

# app.config['MYSQL_DATABASE_HOST'] = 'sql10.freesqldatabase.com'
# app.config['MYSQL_DATABASE_PORT'] = 3306
# app.config['MYSQL_DATABASE_USER'] = 'sql10593302'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'sql10593302'

# app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
# app.config['MYSQL_DATABASE_PORT'] = 3306
# app.config['MYSQL_DATABASE_USER'] = 'sqremates'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'sqremates'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dana'
app.config['MYSQL_DATABASE_DB'] = 'prueba'
mysql.init_app(app)

# inicio el servidor de pruebas flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
