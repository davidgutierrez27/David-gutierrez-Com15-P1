#4 Tabla de multiplicar del 7
#  Objetivo: Usar un bucle para generar patrones.
#  Instrucciones:
# 1. Imprime la tabla de multiplicar del 7 (desde 7x1=7 hasta 7x10=70).
#  Preguntas de reflexión:
# • ¿Cómo adaptarías el código para que el usuario elija la tabla?
# • ¿Qué estructura usarías para almacenar los resultados?


num = 7

for x in range(1, 11):
    resultado = x * num
    print(num, "x", x, "=", resultado)

# • ¿Cómo adaptarías el código para que el usuario elija la tabla?
def pedir_numero():
    num = input("Igrese un num ")
    while  not num.isdigit():
        num = input("ERROR ingrese un num ")
    return int(num)

num = pedir_numero()
for x in range(1, 11):
    resultado = x * num
    print(num, "x", x, "=", resultado)



# • ¿Qué estructura usarías para almacenar los resultados?

def pedir_numero():
    num = input("Igrese un num ")
    while  not num.isdigit():
        num = input("ERROR ingrese un num ")
    return int(num)

num = pedir_numero()
lista=[]
for x in range(1, 11):
    resultado = x * num
    lista.append(f"{num} x {x} = {resultado}")
    print(num, "x", x, "=", resultado)

print(lista)