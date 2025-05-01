# Definición de funciones  
def presentar(nombre, edad):  
    print(f"Hola, soy {nombre} y tengo {edad} años")  

# Programa principal  
presentar("Juan", 30)  # OK  
presentar(30, "Juan")  # ¡El orden es importante!  
presentar(edad=30, nombre="Juan")  # Args con palabra clave  
# presentar(30, nombre="Juan")  # Dos args para el mismo parámetro!  

# print() se puede llamar con args con palabra clave  
print("Uno", "Dos", "Tres")  
print("Uno", "Dos", "Tres", end="\t")  
print("Uno", "Dos", "Tres", sep=",")  
print("Uno", "Dos", "Tres", sep="@", end="FIN")  