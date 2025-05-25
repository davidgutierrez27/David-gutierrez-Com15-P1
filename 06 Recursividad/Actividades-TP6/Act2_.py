#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

# Función recursiva para calcular Fibonacci en una posición
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

def serie_fibonacci(num):
    print(f"Serie de Fibonacci hasta la posición {num}:")
    for i in range(num + 1):    # +1 para incluir la posición 'num'
        print(f"P({i}) = {fibonacci(i)}")

# Mostrar toda la serie hasta la posición dada
print("POSICIÓN DE FIBONACCI")
num = int(input("Ingresa un número (posición máxima): "))
serie_fibonacci(num)
