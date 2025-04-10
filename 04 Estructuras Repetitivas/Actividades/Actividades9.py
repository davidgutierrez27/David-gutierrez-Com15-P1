#9) Elabora un programa que permita al usuario ingresar 100 números enteros
# y luego calcule la media de esos valores.
# (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
     
total = 0
contador = 0

# Pedimos x cantidad de números  
for x in range(100):   
    num = int(input("Ingrese un numero entero: "))  
     
    total += num   
    contador += 1   


# Calcular la media   
media = total / contador  
print("La media de los numeros ingresados es: ", media)
