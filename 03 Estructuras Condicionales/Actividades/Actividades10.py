#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S),
# qué mes del año es y qué día es. El programa deberá utilizar esa información
# para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.  

 

mes = int(input("Mes: "))
dia = int(input("Dia: "))
hemiferio = input("Hemiferio (N/S): ")



if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or (mes < 3):
    if hemiferio == 'N':
        print("Estamos en Invierno")
    else:
        print("Estamos en Verano")

elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (3 < mes < 6):
    if hemiferio == 'N':
        print("Estamos en Primavera")
    else:
        print("Estamos en Otoño")

elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (6 < mes < 9):
    if hemiferio == 'N':
        print("Estamos en Verano")
    else:
        print("Estamos en invierno")

elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (9 < mes < 12):
    if hemiferio == 'N':
        print("Estamos en Otoño")
    else:
        print("Estamos en Promavera")
