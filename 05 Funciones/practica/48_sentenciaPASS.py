# Definición de funciones  
def factorial(num):  
    fact = 1  
    for i in range(num):  
        pass  # Pendiente...  
    return fact  

# Programa principal  
numero = int(input("Ingrese un número natural: "))  
if numero >= 0:  
    el_factorial = factorial(numero)  
    print("El factorial de", numero, "es", el_factorial)  
else:  
    print("No existe el factorial de un número negativo")  