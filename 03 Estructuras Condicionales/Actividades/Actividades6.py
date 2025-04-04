#6)	El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda,
# la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente: 
# from statistics import mode, median, mean  mi_lista = [1,2,5,5,3]  mean(mi_lista) 
# En la documentación oficial se puede encontrar más información sobre este paquete: 
# https://docs.python.org/es/3.8/library/statistics.html.  
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos
# que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ●	Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
# ●	Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# ●	Sin sesgo: cuando la media, la mediana y la moda son iguales. 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios,
# calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma: 
#  import random 
#  numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria. 
 

import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]  #generamos num aletorios

from statistics import mode, median, mean                         #llamamos a las funciones
media = mean(numeros_aleatorios)                                  #almacenamos en una variable los resultaao
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
 
#print("Lista de números aleatorios:", numeros_aleatorios)        #no nos pide pero podemos mostrar los datos para saber  
#print("Moda:", moda)                                             #el valor con que estamos trabajando
#print("Mediana:", mediana)  
#print("Media:", media) 

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")