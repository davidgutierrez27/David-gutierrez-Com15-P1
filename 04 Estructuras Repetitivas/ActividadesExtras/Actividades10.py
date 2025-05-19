#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado
# por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un numero entero: ")) 
num_invertido = 0  


while num > 0:  

    #usamos operador resto (al dividirlo por 10 el resto siempre obtenemos el ultimo digito)
    #(547 % 10 = 7)
    ultimo_digito = num % 10   
    #con esto agregamos el ultimo digito
    #(7+10*0=7)
    num_invertido = num_invertido * 10 + ultimo_digito
    #nos quedamos con la parte entera de la divicion
    # (547 // 10 = 54)  
    num = num // 10  
    
#mostramos el resultado   
print("Número invertido es:", num_invertido)  