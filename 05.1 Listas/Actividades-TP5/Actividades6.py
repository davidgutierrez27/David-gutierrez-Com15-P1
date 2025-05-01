#6) Crear una lista con números del 10 al 30 (incluído),
#  haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

# crear  lista vacia
lista = []
# con un for generamos numeros del 10 a 30 con paso 5
for i in range(10,31,5):
    lista.append(i)

# mostramos los dos primeros
print(lista[0])
print(lista[1])