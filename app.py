#este es un comentario de una sola linia
'''
este es un comentario de multiple linia
con comilla sencilla
'''

"""
este es un comentario de multiple
linia con comilla doble
"""

#Variables
from array import array


nombrePersona = 'yefer' #string
edad = 21 #int entero
numeroDecimal = 10.12 # float flotantes 
esMayorEdad = True #false boleano

#debug 
print(nombrePersona) #yefer

#Array Arreglo Listas [] identificamos que es un arreglo o lista
diasSemana=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
print(diasSemana[2]) #imprimir miercoles

arrayMultiple = [1, 'hola',[5,6]]
print(arrayMultiple[2][1]) #para acceder a un arreglo y dentro de este a una posicion &

#Objetos JSON Diccionarios {}

persona = {
    'nombre':'yefer',
    'apellido':'Lopez',
    'edad':21,
    'lenguajes':['python', 'javascript'],
}

print(persona['apellido'])#Lopez
print(persona['lenguajes'][1])#javascript

#listas de diccionarios
personas = [
{
    'nombre':'yefer',
    'apellido':'Lopez',
    'edad':21,
    'lenguajes':['python', 'javascript'],
},
{
    'nombre':'ivan',
    'apellido':'idrobo',
    'edad':22,
    'lenguajes':['java', '.net'],
},
{
    'nombre':'juan',
    'apellido':'rofriguez',
    'edad':23,
    'lenguajes':['go', 'rust'],
}
]

print(personas[1]['lenguajes'][1])

#condiciones 
if esMayorEdad==True:
    print('es mayor de edad')
else:
    print('no es mayor de edad')

print('terminado')
