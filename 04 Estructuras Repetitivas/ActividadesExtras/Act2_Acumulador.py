#Ejercicio 2: Bucle while con suma acumulativa
# Objetivo: Usar un bucle while para controlar una condición de salida.
# Instrucciones:
#1. Pide al usuario que ingrese números hasta que la suma supere 100.
#2. Imprime la suma total al final.
# Preguntas de reflexión:
#• ¿Qué ocurre si el primer número ingresado es mayor que 100?
#• ¿Cómo evitarías errores si el usuario ingresa texto?



#• ¿Qué ocurre si el primer número ingresado es mayor que 100?
# SI EL NUM ES MAYOR A 100 SE MUESTRA ESE NUM PORQUE NO ENTRARIA AL WHILE

#• ¿Cómo evitarías errores si el usuario ingresa texto?

def pedir_numero():
    num = input("Igrese un num ")
    while  not num.isdigit():
        num = input("ERROR ingrese un num ")
    return int(num)

num = pedir_numero()
suma = num

while suma <= 100:
    num = pedir_numero()
    suma += num

print(suma, "supera a 100, ")