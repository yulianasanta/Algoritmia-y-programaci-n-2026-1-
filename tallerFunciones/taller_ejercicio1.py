"""
Este ejercicio consiste en aplicar los conceptos vistos en clase de funciones para 
analizar una lista de temperaturas que se toma cada hora por un dia. 
En este código se implementan tres funciones: promedio, extremos y dias_sobre_promedio.

prompt: Realizaame un programa en python que calcule el promedio de una lista, determinar el numero mas alto
        y mas bajo de la lista y contar cuantos numeros son mayores al promedio.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
15/04/2026

"""
def promedio(lista):
    """
    Esta función es para calcular el promedio de una
    lista de temperaturas

    Args:
        lista (list): La lista de temperaturas.
    Returns:
        float: El promedio de las temperaturas.
    """
    # Verificar si la lista está vacía.
    if not lista:
        return "Error: Se debe proporcionar una lista no vacía."
    
    #Suma los valores y lo divide entre el total de elementos.
    suma_promedio = sum(lista)
    return suma_promedio / len(lista)

def extremos(lista):
    """
    Esta función cuenta cuantas horas del dia la temperatura
    fue mayor al promedio y cuantas horas fue menor al promedio.

    Args:
        lista (list): La lista de temperaturas.

    Returns:
        tuple: Una tupla con el valor máximo y mínimo.
    """
    # Verificar si la lista está vacía.
    if not lista:
        return "Error: Se debe proporcionar una lista no vacía."
    
    #Utiliza las funciones max y min para encontrar el valor máximo y mínimo en la lista.
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

def dias_sobre_promedio(lista):
    """
    Esta función cuenta cuantas horas del dia la temperatura fue mayor al promedio.

    Args:
        lista (list): La lista de temperaturas.

    Returns:
        int: El número de días sobre el promedio.
    """

    # Verificar si la lista está vacía.
    if not lista:
        return "Error: Se debe proporcionar una lista no vacía."
    
    # Calcula el promedio utilizando la función promedio y luego cuenta cuántos valores en la lista son mayores que el promedio.
    promedio_valor = promedio(lista)
    dias_sobre = sum(1 for valor in lista if valor > promedio_valor)
    return dias_sobre


temperaturas = [20, 22, 21, 19, 18, 24, 25, 23, 21, 20, 22, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
print("Promedio de temperaturas:", promedio(temperaturas))
print("Extremos:", extremos(temperaturas))
print("Días sobre el promedio:", dias_sobre_promedio(temperaturas))