# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.


""" FUNCIONES """
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir entre 0"
    return suma, resta, multiplicacion, division


""" PROGRAMA PRINCIPAL """
# Solicitar los números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Obtener los resultados
suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

# Mostrar los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")