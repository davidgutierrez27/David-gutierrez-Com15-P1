#8)	Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee: 
# 1.	Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2.	Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3.	Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario
# e imprimir el resultado por pantalla.
# 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

 

frase = input("Escriba su nombre: ")
print("ingrese un num (1, 2, 3)")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.") 
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
num =int(input("num: "))

if num == 1:
    # Convertir a mayúsculas  
    frase_mayusculas = frase.upper()  
    print("Frase en mayúsculas:", frase_mayusculas)  
elif num == 2:
    # Convertir a minúsculas  
    frase_minusculas = frase.lower()  
    print("Frase en minúsculas:", frase_minusculas)  
else:
    # Capitalizar  
    frase_ultimaletra = frase.title()
    print("Frase capitalizada:", frase_ultimaletra)
