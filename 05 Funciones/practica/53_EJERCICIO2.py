# Definición de funciones  

    #Lee un número entero del usuario, asegurándose de que esté dentro de los límites dados."""  
def leer_entero_validado(mensaje, min = float('-inf'), max = float('inf')):  
    n = int(input(mensaje))  
    while n < min or n > max:  
        n = int(input("ERROR: " + mensaje))  
    return n  

    #Devuelve el resto de la división entre num1 y num2 sin usar el operador '%'"""  
def obtener_resto(num1, num2):  
    return num1 - (num1 // num2) * num2  

    #Verifica si x es múltiplo de y."""  
def es_multiplo(x, y):  
    return obtener_resto(x, y) == 0  

    #Calcula la suma de los divisores propios de un número (excluyendo el propio número)."""  
def sumatoria_divisores_propios(numero):  
    sumatoria = 0  
    for i in range(1, numero // 2 + 1):  
        if es_multiplo(numero, i):  
            sumatoria += i  
    return sumatoria  

    #Comprueba si un número es perfecto. Un número es perfecto si la suma de sus divisores propios es igual al número."""  
def es_perfecto(numero):  
    return sumatoria_divisores_propios(numero) == numero  

    #Imprime si el número ingresado es perfecto o no."""  
def informar_si_numero_es_perfecto(numero):  
    if es_perfecto(numero):  
        print(f"{numero} es perfecto")  
    else:  
        print(f"{numero} no es perfecto")  

# Programa principal  
num = leer_entero_validado('Ingresa un número natural: ', 1)  
informar_si_numero_es_perfecto(num)  