#6 Números repetidos en una lista
#  Objetivo: Filtrar elementos duplicados manteniendo el orden.
#  Instrucciones:
# 1. Dada una lista (ej: [3, 1, 3, 5, 1]), crea una nueva lista con los números que
# aparecen más de una vez (en este caso: [3, 1]).
#  Preguntas de reflexión:
# • ¿Por qué es importante mantener el orden de aparición?
# • ¿Cómo resolverías esto sin usar estructuras adicionales? 



def pedir_lista():
    lista = []
    while True:
        num = input("Ingresa un número (o 'A' para terminar): ")
        if num.upper() == "A":
            break
        if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):
            lista.append(int(num))
        else:
            print("Entrada inválida, por favor ingresa un número válido.")
    return lista

lista = pedir_lista()
print("Lista ingresada:", lista)
2
vistos = []

for i in lista:
    if i in vistos:
        if i not in repetidos:
            repetidos.append(i)
    else:
        vistos.append(i)

print("Repetidos son: ", repetidos)


# • ¿Por qué es importante mantener el orden de aparición?
# Porque a veces el orden de los datos representa información
# (por ejemplo, el orden de llegada de personas o eventos).
# Alterarlo podría cambiar el significado.


# • ¿Cómo resolverías esto sin usar estructuras adicionales? 
lista = [3, 1, 3, 5, 4, 3, 1]
listafinal = []

for x in lista:
    if lista.count(x) > 1 and x not in listafinal:
        listafinal.append(x)

print(listafinal)
