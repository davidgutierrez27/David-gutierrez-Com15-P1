#3) Escribe un programa que sume todos los números enteros
# comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

#PEDIMOS 2NUMEROS
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese un otro entero: "))  
suma = 0

#INICIALIZAMOS UN BUCLE QUE TOMA LOS DOS VALORES COMO INICIO Y FIN
for x in range(num1+1,num2):            
    suma = suma + x    
print("La suma de sus enteros es", suma)