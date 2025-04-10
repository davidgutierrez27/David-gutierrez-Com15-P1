#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número

#GENERO UN NUM ALEATORIO
import random  
numero_aleatorio = random.randint(0, 9)  # Incluye 0 y 9 


#PEDIMOS 1 NUMERO
print("adivinar un número aleatorio entre 0 y 9:")
num = int(input("Ingresa un numero: "))
acumulador = 0

while num != numero_aleatorio:
    acumulador += 1
    num = int(input("Incorrecto! Ingrese otro: "))

print("¡FELICIDADES! es el numero", numero_aleatorio)
print("Te tomo",acumulador+1,"cantidad de intentos")