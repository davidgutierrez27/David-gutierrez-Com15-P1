# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)



""" FUNCIONES """

def suma_digitos(n):
#    while n != 0:
#         acu += n % 10
#         n = n // 10
#     return acu
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)


""" PROGRAMA PRINCIPAL """
num = int(input("Ingrese un num: "))
print(suma_digitos(num))