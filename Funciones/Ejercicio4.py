# Invertir cadena
"""
Este código es para realizar una función que invierta los 
caracteres de una palabra.

Prompt: Escribe una función recursiva llamada invertir_cadena(texto)
que reciba un string y lo devuelva invertido.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
11/04/2026
"""

def invertir_cadena(texto):
    """
    Recibe un string y lo devuelve invertido utilizando recursión.

    Args:
        texto (str): La cadena de texto inicial.

    Returns:
        str: La cadena de texto invertida.
    """
    if len(texto) <= 1:
        return texto
    """
    Cuenta cuantos elementos tiene la lista y si
    es menor a o igual a 1 devolver el mismo texto.
    """

    return texto[-1] + invertir_cadena(texto[:-1])
    """
    Toma el ultimo caracter de la lista y lo pone
    al inicio y lo hace con el resto de la cadena.
    """
texto = str(input("ingrese la palabra: "))
resultado = invertir_cadena(texto)

print(f"Original: {texto}")
print(f"Invertida: {resultado}")
