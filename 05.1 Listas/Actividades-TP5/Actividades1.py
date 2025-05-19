#1) Crear una lista con los números del 1 al 100
# que sean múltiplos de 4. Utilizar la función range.


numeros = list(range(1, 101))      # Crear la lista de números del 1 al 100
multiplos4 = []                # Crear una lista vacía donde guardar los múltiplos de 4
for n in numeros:            # Recorrer cada número en la lista y verificar si es múltiplo de 4
    if n % 4 == 0:
        multiplos4.append(n)

print(multiplos4)



# Despues lo corregi a esto es mas practico
# multiplos4 = range(4, 101, 4)
# print(list(multiplos4))