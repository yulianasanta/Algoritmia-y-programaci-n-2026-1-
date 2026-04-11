# Filtro y tranformación recursiva
"""
Este es un código para implementar resusividad en lugar de usar
dos funciones diferentes (filter y map). Este codigo recorre una
lista de números determina cual de estos es par y lo eleva al cuadrado
si no es par lo deja pasar al final imprime el resultado de la lista
original y los numeros elevados al cuadrado.

Prompt: Realiza un código para python el cual solucione el
siguiente problema: En lugar de usar filter y map, crearemos una función que recorra
una lista, decida si un número es par y, si lo es, lo eleve al cuadrado,
todo en un solo paso recursivo.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
fecha:
"""
def procesar_lista_recursiva(lista):
    """
    Recorre una lista, filtra los números pares y los eleva al cuadrado
    usando recursividad en un solo paso.

    Args:
        lista: Es el conjunto de números que se quiere procesar

    Returns:
        Resultado: Una nueva lista filtrada y transformada

    """
    if not lista:
        return []
    """
    Esta función hace que si la lista queda vacia pare y devuelva 
    la lista vacia
    """
    primero = lista[0]
    resto = lista[1:]
    """
    Se toma el primer número y deja el resto para 
    revisarlos despues. Eso es lo que recorre la lista.
    """

    if primero % 2 == 0:
        """
        Esta condición coge el primer número y lo divide entre dos
        si el residuo es cero significa que el numero es par.
        """
        valor_transformado = primero ** 2
        """
        Si es par lo eleva al cuadrado
        """
        return [valor_transformado] + procesar_lista_recursiva(resto)
    else:

        return procesar_lista_recursiva(resto)
    """
    se usa el operador + para ir pegando los resultados. 
    Si el número era par pegamos el cuadrado del número y si 
    no era par no paga nada y devuelve lo que vanga en las 
    siguientes llamadas.
    """

numeros_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = procesar_lista_recursiva(numeros_entrada)

print(f"Lista original: {numeros_entrada}")
print(f"Resultado (pares al cuadrado): {resultado}")
