# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.



""" FUNCIONES """
def calcular_promedio(a, b, c):
    return (a + b + c) / 3



""" PROGRAMA PRINCIPAL """
# Solicitar  al usuario
num1 = int(input("Ingrese num1: "))
num2 = int(input("Ingrese num2: "))
num3 = int(input("Ingrese num3: "))

promedio = calcular_promedio(num1, num2, num3)

# Mostrar los resultados
print(f"El promdeio de {num1}, {num2}, {num3} es: {promedio}")