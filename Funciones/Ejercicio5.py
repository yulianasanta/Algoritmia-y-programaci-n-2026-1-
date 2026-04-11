#Numero maximo
"""
Este es un código el cual se basa en buscar el número mayor en
una determinada lista.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
11/04/2026
"""
def buscar_maximo(lista):
    """
    Encontrar el valor maximo de una lista

    Args:
        lista (list): Es la lista de la cual se quiere saber que número es mayor

    Returns:
        int: El número mas grande encontrado en la [Lista]
    """
    if len(lista) == 1:
        return lista[0]
    """
    Cuenta cuantos elemetos de la lsita y si solo hay uno retorna el
    elemto de la posicion 0.
    """

    max_del_resto = buscar_maximo(lista[1:])
    """
    Nombra una variable que recoge el resto de la lista (despues de la 1ra posición).
    """
    
    primero = lista[0]
    """
    Nombra otra variable que evalue la primera posición.
    """
    
    if primero > max_del_resto:
        return primero
    else:
        return max_del_resto
    """
    Evalua el primer número de la lista y lo compara con el 
    resto de la lista si es mayor retorna el primer número, 
    si no vuelve a evaluar.
    """

lista = [2, 4, 5, 10, 50, 8,]
print(f"El número más grande es: {buscar_maximo(lista)}")
