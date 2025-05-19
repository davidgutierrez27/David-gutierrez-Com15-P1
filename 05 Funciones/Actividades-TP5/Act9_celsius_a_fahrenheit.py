# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.


""" FUNCIONES """
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

""" PROGRAMA PRINCIPAL """
# Solicitar  al usuario
temperatura = float(input("Ingrese la temperatura actual en (celsius): "))
fahrenheit = celsius_a_fahrenheit(temperatura)

# Mostrar los resultados
print(f"{temperatura}º celsius es equivalente a: {fahrenheit}º fahrenheit")