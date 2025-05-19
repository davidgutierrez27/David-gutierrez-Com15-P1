#Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes.
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.


""" FUNCIONES """

def segundos_a_horas(segundos):
    horas = segundos // 3600                 #nos quedamos solo con la parte entera osea el redondo en hs
    minutos = (segundos % 3600) // 60        #el sobrante rensto, lo dividimos por 60 y asi tambien lop tenemos
    return horas, minutos



""" PROGRAMA PRINCIPAL """
# Solicitar al usuario
seg = int(input("Ingrese una cantidad de segundos: "))

h, m = segundos_a_horas(seg)
print(f"{seg} segundos equivalen a: {h} horas y {m} minutos")
