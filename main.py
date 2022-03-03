from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)#instancia

@app.get("/")#creando ruta
def index():
    return render_template("index.html")

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