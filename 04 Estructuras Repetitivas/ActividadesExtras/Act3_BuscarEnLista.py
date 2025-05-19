#jercicio 3: Filtrar palabras por letra inicial
#  Objetivo: Iterar sobre una lista y aplicar filtros.
#  Instrucciones:
# 1. Dada una lista de palabras (ej: ["apple", "banana", "avocado"]), imprime
# solo las que empiezan con "a".
#  Preguntas de reflexión:
# • ¿Cómo harías que la comparación sea case-insensitive (ej: "Apple" también
# se cuente)?
# • ¿Qué método de strings es útil para esto?



lista = ["apple", "banana", "avocado"]

for palabra in lista:  #TOMA CADA PALABRA DE LA LISTA (FOR X IN LISTA(3 or 5 or 8etc)
    if palabra[0] == "a":  
        print(palabra)       



# • ¿Cómo harías que la comparación sea case-insensitive (ej: "Apple" también
# se c
lista = ["apple", "banana", "avocado"]

for palabra in lista:
    if palabra[0] == "a" or palabra[0] == "A":
    #if palabra[0].lower() == "a":  
        print(palabra)  


# • ¿Qué método de strings es útil para esto?
"banana".startswith("b")       # True
"banana".startswith("ba")      # True
"banana".startswith("a")       # False
"Banana".startswith("b")       # False (porque es mayúscula)

# Versión sin importar mayúsculas:
"Banana".lower().startswith("b")  # True
