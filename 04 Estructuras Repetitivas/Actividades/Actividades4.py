#4) Elabora un programa que permita al usuario ingresar números enteros
# y los sume en secuencia.
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0


#PEDIMOS 1 NUMERO
num = int(input("Ingrese un numero entero: "))
acumulador = 0

while num != 0:
    acumulador += num
    num = int(input("Ingrese un numero entero: "))

print("La suma de sus enteros ingresados en secuencias es", acumulador)