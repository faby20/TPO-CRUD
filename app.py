# de flask que importamos estamos trayendo flask(para crear el objeto flask), jsonify y request para deinir ruta, con http vamos a hacer la comunicacion back, front con pedido y peticion
from flask import Flask ,jsonify ,request
# para crear una instancia cors, para comsumir el backend
from flask_cors import CORS
# para crear el esquema de la base de datos
from flask_sqlalchemy import SQLAlchemy
# para hacer la parte del consumo, que nos traigan distintas cosas de la base de datos
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/tpo_2_crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
ma = Marshmallow(app)

#BBDD, crear el modelo, usando clases
# va a heredar un modelo de sql alchemy
class Producto(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Float())
    stock = db.Column(db.Integer) # se guarda la url
    imagen = db.Column(db.String(400))

    def __init__(self,nombre,precio,stock,imagen):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.imagen = imagen

# crear un contexto para que la base de datos sea creado en la q definimos
with app.app_context():
    db.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','stock','imagen')

producto_schema=ProductoSchema()                #para almacenar 1 producto
productos_schema=ProductoSchema(many=True)        #para almacenar muchos productos

# crear los endpoints o rutas
@app.route('/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all() 
    resultado = productos_schema.dump(productos) #no strae todos los datos de la tabla
    return jsonify(resultado)

@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto = Producto.query.get(id) 
    return producto_schema.jsonify(producto) #retorna el json de un producto recibido

@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto = Producto.query.get(id) 
    db.session.delete(producto)
    db.session.commit()#para q el cambio sea guardado
    return producto_schema.jsonify(producto) #retorna el eliminado

#post, para crear un producto
@app.route('/productos', methods=['POST'])
def create_producto():
    #cualquier pedido que me hace el usuario al apretar un boton, me crea un producto en la base de dtos
    nombre = request.json['nombre'] 
    precio = request.json['precio'] 
    stock = request.json['stock'] 
    imagen = request.json['imagen']
    #crea una variable que va a guardar las instancias q se crearon antes
    nuevo_producto = Producto (nombre, precio, stock, imagen)
    db.session.add(nuevo_producto)
    db.session.commit()
    return producto_schema.jsonify(nuevo_producto)

@app.route('/productos/<id>', methods=['PUT'])
def update_producto(id):
    producto = Producto.query.get(id)
    nombre = request.json['nombre'] 
    precio = request.json['precio'] 
    stock = request.json['stock'] 
    imagen = request.json['imagen']

    producto.nombre = nombre
    producto.precio = precio
    producto.stock = stock
    producto.imagen = imagen
    db.session.commit()
    return producto_schema.jsonify(producto)

if __name__ =='__main__':
    app.run(debug=True, port=5000)

#las unicas rutas q se oueden ver son las q tienen get








