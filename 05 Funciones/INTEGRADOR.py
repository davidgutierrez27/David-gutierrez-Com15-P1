import random

# VARIABLES

# ARRAY CON LOS NUMEROS QUE ADMITE EL PROGRAMA (DEL 0 AL 15)
opciones = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]


# FUNCIONES

# RETORNA TRUE SI LOS PARAMETROS ENVIADOS SON IGUALES, FALSE SI NO
def son_iguales(primer_valor, segundo_valor):
    return primer_valor == segundo_valor
    # return V / F

def binario_a_decimal(binario):
    decimal = int(binario, 2)
    return decimal
 # División | Cociente | Resto
 # 13 ÷ 2   |  6       | 1
 # 6 ÷ 2    |  3       | 0
 # 3 ÷ 2    |  1       | 1
 # 1 ÷ 2    |  0       | 1

def jugar_ronda():

    # SELECCIONO UN NUMERO ALEATORIO DEL ARRAY DE BINARIOS
    valor_a_convertir = random.choice(opciones)

    # CONVIERTO EL NUMERO BINARIO A DECIMAL
    respuesta_correcta = binario_a_decimal(valor_a_convertir)

    print(f"EL NUMERO BINARIO A CONVERTIR ES: {valor_a_convertir}")
    print("--------------------------------------------")

    # RESPUESTA DEL USUARIO
    respuesta_usuario = int(input("INGRESE SU RESPUESTA: "))

    # CANTIDAD DE INTENTOS
    cantidad_intentos = 1

    while not son_iguales(respuesta_correcta, respuesta_usuario):

        print("--------------------------------------------")
        print("RESPUESTA INCORRECTA 🙁")

        respuesta_usuario = int(input("VOLVE A INTENTAR: "))
        cantidad_intentos += 1

    if cantidad_intentos == 1:
        print("EXCELENTE! ACERTASTE A LA PRIMERA 💪")
    elif cantidad_intentos >= 2 and cantidad_intentos < 4:
        print("MUY BIEN! ESTUVISTE CERCA DE ACERTAR A LA PRIMERA 😎")
    elif cantidad_intentos >= 4 and cantidad_intentos < 8:
        print("COSTÓ UN POQUITO, PERO LO LOGRASTE 👏")
    else:
        print("LO IMPORTANTE ES QUE NO TE DISTE POR VENCIDO 😅")


# PROGRAMA PRINCIPAL

print("CONVERSION DE BINARIOS A DECIMALES")
print("--------------------------------------------")

continuar = 'S'

while continuar != "N":

    jugar_ronda()
    print("--------------------------------------------")
    continuar = input("¿QUERES VOLVER A JUGAR? INGRESE S (SI) O N (NO): ").upper()