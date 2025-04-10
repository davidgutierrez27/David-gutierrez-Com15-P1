#7) Crea un programa que calcule la suma de todos los números comprendidos
# entre 0 y un número entero positivo indicado por el usuario.
    
    
#PEDIMOS UN NUMEROS
num = int(input("Ingrese un numero entero positivo: "))  
suma = 0

#VALIDACION
while num <= 0:
    num = int(input("Debe Ingresar un numero entero positivo: "))

#CICLO 
if num > 0:
    for x in range(num):            
        suma = suma + x    
    print("La suma de los valores comprendidos entre 0 y",num,"es;",suma)
    