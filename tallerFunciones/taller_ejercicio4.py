"""
 Este es un programa para la clase de algoritmia y programacion
 de el profesor Juan Pablo Escobar Vargas, el cual se basa en diseñar 
 un programa para el prosesamientos de calificaciones de estudiantes.
 Incluyendo promedio simple, promedio ponderado por poncertanjes, tambien
 identificando el estudiante con el mejor promedio y mostrando los 
 estudiantes aprobados y reprobados.

prompt: Realiza un programa en python que permita calcular el promedio simple 
        y ponderado de las notas de los estudiantes, identificar el estudiante 
        con el mejor promedio y mostrar los estudiantes aprobados y reprobados.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
17/14/2026
"""

def promedio_simple(lista_notas):
    """
    Esta función es para calcular el promedio simple de una lista de notas.
    Args:
        lista_notas (list): La lista de notas de un estudiante.
    
    Returns:
        float: El promedio simple de las notas.
    """
    return sum(lista_notas)/len(lista_notas)

def promedio_ponderado(lista_notas):
    """
    Esta función es para calcular el promedio ponderado de una lista de notas,
    utilizando los siguientes porcentajes: 30% para la primera nota, 30% para
    la segunda mota y 40% para la tercera nota.

    Args:
        lista_notas (list): La lista de notas de un estudiante.
    
    Returns:
        float: El promedio ponderado de las notas.
    """
    n1= lista_notas[0] * 0.30
    n2 = lista_notas[1] * 0.30
    n3 = lista_notas[2] * 0.40
    return n1+n2+n3

def mayor_promedio(diccionario):
    """
    Esta función es para identificar el estudiante con el mejor promedio ponderado.

    Args:
        diccionario (dict): Un diccionario que contiene los nombres de los estudiantes 
        como claves y sus notas como valores.

    Returns:
        tuple: Una tupla con el nombre del estudiante con el mejor promedio y su promedio.
    """
    nombre_m = "nombre"
    promedio_m = -1

    for nombre, lista in diccionario.items():
        promedio = promedio_ponderado(lista)
        if promedio > promedio_m:
            promedio_m = promedio
            nombre_m = nombre
    return nombre_m, promedio_m

def aprobados(diccionario):
    """
    Esta función es para mostrar los estudiantes aprobados, es decir, aquellos con un promedio 
    ponderado de 3.0 o más.

    Args:
        diccionario (dict): Un diccionario que contiene los nombres de los estudiantes 
        como claves y sus notas como valores.
    
    """
    print("Lista de estudiantes aprobados")
    for nombre, lista in diccionario.items():
        promedio_general=promedio_ponderado(lista)
    if promedio_general >= 3.0:
        print(f"Estudiante {nombre} | promedio {promedio_general}")

def reporte_profesora(diccionario):
    """
    Esta función es para mostrar un reporte de cada estudiante indicando si aprobó o 
    reprobó la clase de transformaciones, considerando que el promedio ponderado de 
    aprobación es de 3.0 o más.

    Args:
        diccionario (dict): Un diccionario que contiene los nombres de los estudiantes 
        como claves y sus notas como valores.
    
    """
    for nombre, lista in diccionario.items():
        promedio_general = promedio_ponderado(lista)
        if promedio_general >= 3.0:
            print(f"{nombre} aprobó la clase de transformaciones con {promedio_general}.")
        else:
            print (f"{nombre} reprobó la clase de transformaciones con {promedio_general}.")

#Ejecucion del programa

#base de datos de los estudiantes y sus notas
notas = {
    "Harry": [3.8, 4.0, 4.2],
    "Ron": [3.2, 3.8, 2.8],
    "Hermione":[5.0,5.0,5.0],
    "Draco":[4.5,4.2,5.0],
    "Nevil":[2.5,3.0,3.2]
    }

print("Resultados Individuales: ")
for nombre, lista in notas.items():
    simple=promedio_simple(lista)
    ponderado=promedio_ponderado(lista)
    print(f"El Estudiante {nombre} tiene un promedio simple de {simple} y un promedio ponderado de {ponderado}.")


mejor_n , mejor_p = mayor_promedio(notas)
print(f"El estudiante con mayor promedio es {mejor_n} con {mejor_p}")

print(aprobados(notas))

print(reporte_profesora(notas))