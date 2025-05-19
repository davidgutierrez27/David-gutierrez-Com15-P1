#11: Bucle for para números pares
# Objetivo: Imprimir números pares usando un bucle for.
# Instrucciones:
#1. Escribe un bucle for que imprima los números pares del 2 al 20 (inclusive).
#2. Usa un condicional o el paso del rango para lograrlo.
# Preguntas de reflexión:
#• ¿Cómo modificarías el código para imprimir solo impares?
#• ¿Qué pasa si el rango fuera de 2 a 20 con paso 3?

print("PARA NUM PARES")
for num in range(2,21):
    if num % 2 == 0:
        print(num)


#• ¿Cómo modificarías el código para imprimir solo impares?
print("PARA NUM IMPARES")
for num in range(2,21):
    if not(num % 2 == 0):
        print(num)

#¿Qué pasa si el rango fuera de 2 a 20 con paso 3?
print("PARA 2 a 20 con paso 3")
for num in range(2,21,3):
    if num % 2 == 0:
        print(num)