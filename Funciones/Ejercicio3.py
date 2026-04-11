# Suma Recursiva
"""
Este codigo es para realizar una funcion que suma los elemtos de
una lista dividiendo la lista en el elemto en la posicion 0 y el
resto de la lista. Se llama a si para hacerla repetidamente hasta
haata que no queden mas elemtos.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
fecha:
"""

def suma_recursiva(lista):
    """
    Calcula la suma de todos los elemtos de una lista de forma 
    recursiva.

    Args:
        lista (float): la lista de la cual se desean sumar los números.

    Returns:
        resultado: Entrega la suma de los números de la lista inicial.
    """
    if not lista:
        return 0
        """
        si no se encuentra la números en la lista retornar a cero
        """
    return lista[0]+ suma_recursiva(lista[1:])
    """
    si se encuentra núeros sumar el que esta en la primera posición
    sumarlo con el de la segunda posición y repetir hasta que no se
    encuentren mas digitos
    """

lista=[1,8.5,30,40]
resultado = suma_recursiva(lista)

print(f"la suma de la lista{lista} es {resultado}")
