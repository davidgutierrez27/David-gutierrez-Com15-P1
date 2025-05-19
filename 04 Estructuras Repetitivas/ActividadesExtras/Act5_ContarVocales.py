#5: Contador de vocales
#  Objetivo: Contar caracteres específicos en un string.
#  Instrucciones:
# 1. Pide al usuario una cadena de texto.
# 2. Cuenta y muestra cuántas vocales (a, e, i, o, u) contiene.
#  Preguntas de reflexión:
# • ¿Cómo manejarías las vocales acentuadas (á, é)?
# • ¿Qué estructura de datos te ayudaría a optimizar el código?


def pedir_string():
    cadena = input("Ingresa una frase: ")
    while not cadena:  # Validamos que no esté vacía
        cadena = input("ERROR. Ingresa una frase válida: ")
    return cadena

# Función para contar vocales simples
def contar_vocales(texto):
    contador = 0
    vocales = "aeiouAEIOU"  # Aceptamos mayúsculas también
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

# Uso
cadena = pedir_string()
total = contar_vocales(cadena)
print("Cantidad de vocales:", total)


# • ¿Cómo manejarías las vocales acentuadas (á, é)?
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"


# • ¿Qué estructura de datos te ayudaría a optimizar el código?
# ✅ Un set (conjunto) es más rápido que una cadena o lista para búsquedas:
vocales = {'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'}
# Porque el in en un set es más eficiente que en una cadena o lista.