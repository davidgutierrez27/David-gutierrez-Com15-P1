#8) Escribe un programa que permita al usuario ingresar 100 números enteros.
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares,
# cuántos son negativos y cuántos son positivos.
# (Nota: para probar el programa puedes usar una cantidad menor,
# pero debe estar preparado para procesar 100 números con un solo cambio).
  
cont_pos = 0
cont_neg = 0
cont_ceros = 0
cont_pares = 0
cont_inpares = 0

#Pedimos x camtidad de numeros (en este caso prove con 10 pero podria poner los 100)
for x in range(10):#podes cambiar a 100
    num = int(input("Ingrese un numero entero positivo: "))

    if num > 0:
        cont_pos += 1
    elif num < 0:
        cont_neg += 1
    else:
        cont_ceros += 1

    if num % 2 == 0:
        cont_pares += 1
    else:
        cont_inpares += 1

print("Cantidad de positivos: ",cont_pos)
print("Cantidad de negativos: ",cont_neg)
print("Cantidad de ceros: ",cont_ceros)
print("Cantidad de pares: ",cont_pares)
print("Cantidad de inpares: ",cont_inpares)
