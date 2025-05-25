#Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛 ** 𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
# . Prueba esta función en un


# algoritmo general.

#  def potencia(base, exponente):
#      res = base * base ** (exponente - 1)
#      print(res)

#  base = int(input("Ingrese la base: "))
#  exponente = int(input("Ingrese un exponente: "))
#  potencia(base,exponente)



def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return  base * potencia(base, exponente - 1)
    

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese un exponente: "))
res = potencia(base,exponente)

print(res)