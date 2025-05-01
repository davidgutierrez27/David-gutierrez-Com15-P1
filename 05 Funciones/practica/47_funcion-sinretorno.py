# Definición de funciones  
def imprimir_simbolo(simbolo, veces):  
    for i in range(veces):  
        print(simbolo, end="")  
    print()  # Salto de línea  

def sucesion_simbolos(simbolo, veces):  
    sucesion = ""  
    for i in range(veces):  
        sucesion += simbolo  # Concatenando simbolo a sucesion  
    return sucesion  

# Programa principal  
imprimir_simbolo("@", 8)  
imprimir_simbolo("*", 14)  
imprimir_simbolo("Z", 6)  

los_pesos = sucesion_simbolos("$", 20)  
print(los_pesos)  