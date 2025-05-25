#Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.


""" FUNCIONES """

def informacion_personal(nombre, apellido, edad, residencia):
    print("Soy", nombre, apellido, "tengo", edad, "años y vivo en", residencia)



""" PROGRAMA PRINCIPAL """

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
edad = input("Escribe tu edad: ")
residencia = input("Escribe tu residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
