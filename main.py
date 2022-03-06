
from flask import Flask, render_template, request, redirect, url_for

import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='productos',
    port=3306
)

db.autocommit = True
app = Flask(__name__)#instancia

@app.get("/")#creando ruta
def index():
    cursor= db.cursor(dictionary=True)

    cursor.execute('select * from productos')
    productos = cursor.fetchall()    #trae todos los valores de la lista
    #productos = cursor.fetchone() #trae el primero de la lista
    print(productos[1]['nombre'])

    cursor.close()

    return render_template("index.html", productos=productos)

@app.get("/crear")
def crearProducto():
    return render_template("crear.html")

@app.post("/crear")
def crearProductoPost():
    nombre = request.form.get('nombre')#nombre es variable (nombre) es el name="nombre" del formulario
    precio = request.form.get('precio')

    cursor = db.cursor() #como se va a insertar datos es decesario el diccionario}
    
    cursor.execute("insert into productos(nombre, precio) values(%s,%s)", (
        nombre,
        precio,
    ))
    
    
    cursor.close()

    return redirect(url_for('index'))
    
@app.get("/contacto")
def contacto():
    return render_template("contactos/index.html")

@app.get("/contacto/<int:contactoId>/edit")#ruta con parametros --contactoid es cualquier variable
def editarContacto(contactoId):
    suma= 2+2
    return render_template("contactos/editar.html", contactoId=contactoId, suma=suma)#id=contactoId puede ser cualquier nombre la variable
    
#/edad/27 tu naciste en el año: 
@app.get("/contacto/<int:edadP>/edad")
def edadpersona(edadP):
    
    return render_template("contactos/edad.html",
                           edadP = edadP)
app.run(debug=True)