# Función para leer un entero validado dentro de un rango  
def leer_entero_validado(mensaje, min=float("-Inf"), max=float("Inf")):  
    n = int(input(f"{mensaje}: "))  
    while n < min or n > max:  # Validar que el número esté dentro del rango  
        n = int(input(f"ERROR. {mensaje}: "))  
    return n  

# Función para obtener el resto de dos números sin usar el operador %  
def obtener_resto(num1, num2):  
    return num1 - num2 * (num1 // num2)  # Usa división entera para calcular el resto  

# Función para verificar si x es múltiplo de y  
def es_multiplo(x, y):  
    return obtener_resto(x, y) == 0  # Verifica si el resto es cero  

# Función para determinar si un número es primo  
def es_primo(numero):  
    cont = 2  # Contador de divisores  
    mitad = numero // 2  # Mitad del número para limitar las verificaciones  
    # Verificamos divisores hasta la mitad del número  
    while cont <= mitad and not es_multiplo(numero, cont):  
        cont += 1  # Incrementar el contador de divisores  
    return cont > mitad  # Si cont no superó mitad, el número es primo  

# Función para informar si un número es primo  
def informar_si_numero_es_primo(numero):  
    if es_primo(numero):  
        print(f"El número {numero} es primo")  # Mensaje si el número es primo  
    else:  
        print(f"El número {numero} NO es primo")  # Mensaje si el número no es primo  







# Programa principal  
num = leer_entero_validado("Ingrese un número natural", 1)  # Leer un número natural  
informar_si_numero_es_primo(num)  # Informar si el número es primo  