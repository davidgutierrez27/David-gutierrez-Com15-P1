# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC).
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado
#  con dos decimales.


""" FUNCIONES """
def calcular_imc(peso, altura):
    imc = round((peso / (altura ** 2)), 2) #redondeamos a dos cifras
    if 18.5 > imc < 24.99:
        peso = "peso normal"
    elif imc >= 25:
        peso = "sobrepeso"
    elif imc < 18.5:
        peso = "delgado"

    return imc , peso


""" PROGRAMA PRINCIPAL """
# Solicitar los números al usuario
altura = float(input("Ingrese altura (metros): "))
peso = float(input("Ingrese peso (kg): "))

imc, peso = calcular_imc(peso,altura)

# Mostrar los resultados
print(f"Su masa corporala es de: {imc}")
print(f"Usted esta en la clasificaion de: {peso}")