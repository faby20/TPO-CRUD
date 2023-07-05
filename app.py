# de flask que lo importamos estamos traendo flask(para crear el objeto flask), jsonify y request para deinir ruta, con http vamos a hacer la comunicacion back, front con pedido y peticion
from flask import Flask ,jsonify ,request
# para crear una instancia cors, para comsumir el backend
from flask_cors import CORS
# para crear el esquema de la base de datos
from flask_sqlalchemy import SQLAlchemy
# para hacer la parte del consumo, que nos traigan distintas cosas de la base de datos
from flask_marshmallow import Marshmallow

app = Flask(_name_)