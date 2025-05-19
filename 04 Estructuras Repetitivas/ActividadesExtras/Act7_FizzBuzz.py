#7: FizzBuzz
#  Objetivo: Implementar lógica condicional en bucles.
#  Instrucciones:
# 1. Imprime números del 1 al 100, pero:
# o Para múltiplos de 3 → "Fizz".
# o Para múltiplos de 5 → "Buzz".
# o Para múltiplos de ambos → "FizzBuzz".
# Preguntas de reflexión:
# • ¿Por qué el orden de los condicionales es crucial aquí?
# • ¿Cómo extenderías el juego a otros números (ej: 7 → "Bazz")?

print("IMPRIMIR NÚMEROS DEL 1 AL 100")
print("Para múltiplos de 3 → Fizz")
print("Para múltiplos de 5 → Buzz")
print("Para múltiplos de 7 → Bazz")
print("Combinaciones posibles: FizzBuzz, FizzBazz, BuzzBazz, FizzBuzzBazz")

for x in range(1, 101):
    salida = ""

    if x % 3 == 0:
        salida += "Fizz"
    if x % 5 == 0:
        salida += "Buzz"
    if x % 7 == 0:
        salida += "Bazz"

    if salida:
        print(salida)
    else:
        print(x)


# ¿por qué el orden es importante?
# La condición x % 3 == 0 and x % 5 == 0 debe ir primero,
# porque si ponés primero x % 3 == 0, ya va a imprimir "Fizz"
# para los múltiplos de 15, y nunca llegará a "FizzBuzz".