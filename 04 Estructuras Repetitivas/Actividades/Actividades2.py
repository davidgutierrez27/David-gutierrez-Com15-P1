#Desarrolla un programa que solicite al usuario un número entero
# y determine la cantidad de dígitos que contiene


num = int(input("Ingrese un numero entero: "))
cadena = str(num)
contador = 0
 
numero_de_caracteres = len(cadena)  #usando len para contar la cadena y guardar en una variable 
print(numero_de_caracteres)  
  

for x in cadena:            #usando for con una cadena ya que iterna n catidad de caracteres que tenga
    contador += 1    
print("La cantidad de digito de", num, "es", contador)