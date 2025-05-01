# Definición de funciones  
def factorial(num):  
    global numero  # Variable global  
    fact = -1  # Inicialización de la variable global  
    print(f"El número global es {numero}")  
    for i in range(1, num + 1):  
        fact *= i  # Multiplicando por el índice  
    return fact  

# Programa principal  
numero = int(input("Ingrese un número natural: "))  # Variable global  
if numero >= 0:  
    fact = factorial(numero)  
    print("El factorial de", numero, "es", fact)  
else:  
    print("No existe el factorial de un número negativo")  