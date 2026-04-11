# Invertir cadena

def invertir_cadena(texto):
    """
    Recibe un string y lo devuelve invertido utilizando recursión.

    Args:
        texto (str): La cadena de texto original.

    Returns:
        str: La cadena de texto invertida.
    """
    # 1. Caso Base: Si la cadena está vacía o tiene un solo carácter,
    # ya está "invertida", así que la devolvemos tal cual.
    if len(texto) <= 1:
        return texto

    # 2. Paso Recursivo:
    # Tomamos el último carácter y lo ponemos al principio,
    # luego llamamos a la función con el resto de la cadena.
    return texto[-1] + invertir_cadena(texto[:-1])

texto = str(input("ingrese la palabra: "))
resultado = invertir_cadena(texto)

print(f"Original: {texto}")
print(f"Invertida: {resultado}")