#Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función


""" FUNCIONES """

def tabla_multiplicar(numero):
    print("La tabla de", numero, "es:")
    for x in range(1,11):
        print(numero, "x" , x, "=",(numero*x))



""" PROGRAMA PRINCIPAL """

num = int(input("Que tabla necesitas: "))
tabla_multiplicar(num)