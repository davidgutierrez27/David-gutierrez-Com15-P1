# Definición de funciones  
def presentar(nombre="anónimo", edad=50):  
    # Los parámetros pro default deben ir siempre al final  
    print(f"Hola, soy {nombre} y tengo {edad} años")  

# Programa principal  
presentar("Juan", 27)  # Ambos argumentos  
presentar("María")      # Solo primer argumento  
presentar()             # Sin argumentos  
presentar(43)          # El orden de los argumentos es importante  

input("Ingresa algo...")  
input()  