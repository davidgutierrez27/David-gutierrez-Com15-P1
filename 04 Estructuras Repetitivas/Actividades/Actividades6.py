#6) Desarrolla un programa que imprima en pantalla todos los números pares
# comprendidos entre 0 y 100, en orden decreciente.


#ACA DEJO MI PRIMER INTENTO
#num = 100
#for x in range(100):
#    if num % 2 == 0:
#        print(num)  
#    num -= 1
    
    
# INICIA EN 100 HASTA 0 
# De 100 a 0, incluyendo 0, con paso -1 
for num in range(100, -1, -1):   
    if num % 2 == 0:   
        print(num)  