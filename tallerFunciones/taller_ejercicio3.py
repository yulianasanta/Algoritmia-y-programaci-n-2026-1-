"""
Este ejercicio se realizo un código para aplicar conceptos adquiridos en clase
de funciones para realizar un sistema de inventario, el cual tiene las funciones
de agregar producto, eliminar producto, calcular el valor total del inventario y 
mostrar el inventario.

Prompt: Realiza un programa en python que permita agregar productos a un inventario, 
        eliminar productos, calcular el valor total del inventario y mostrar el inventario.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
15/04/2026
"""

def agregar_producto(diccionario, nombre, cantidad, precio):
    """
    Esta función permite agrega un producto o actualiza sus valores si 
    ya existe.
    
    Args:
        diccionario (dict): El diccionario que representa el inventario.
        nombre (str): El nombre del producto.
        cantidad (int): La cantidad del producto.
        precio (float): El precio del producto.
    Returns:
        None: No devuelve ningún valor, pero actualiza el diccionario de inventario.
    """
    diccionario[nombre] = {
        "cantidad": cantidad, 
        "precio": precio
    }
    print(f"Se agrego {nombre} al inventario")

def eliminar_producto(diccionario, nombre):
    """Esta funcion elimina un producto del diccionario si existe.
    
    Args:
        diccionario (dict): El diccionario que representa el inventario.
        nombre (str): El nombre del producto a eliminar.
    
    Returns:
        None: No devuelve ningún valor, pero actualiza el diccionario de inventario.
    """
    if nombre in diccionario:
        diccionario.pop(nombre)
        print("Producto eliminado:", nombre)
    else:
        print("Error: El producto no existe en el inventario.")

def calcular_valor_total(diccionario):
    """
    Esta función es para calcular la suma del costo total (cantidad * precio) de todos 
    los productos.

    Args:
        diccionario (dict): El diccionario que representa el inventario.
    Returns:
        float: El valor total del inventario.

    """
    total = 0
    for datos in diccionario.values():
        total += datos["cantidad"] * datos["precio"]
    return total

def mostrar_inventario(diccionario):
    """
    Imprime el contenido actual del inventario.

    Args:
        diccionario (dict): El diccionario que representa el inventario.
    
    Returns:
        None: No devuelve ningún valor, pero imprime el inventario en la consola.
    """
    print("--- LISTA DE INVENTARIO ---")
    if not diccionario:
        print("El inventario esta vacio.")
    else:
        for nombre, datos in diccionario.items():
            print(f"Producto: {nombre} | Cantidad: {datos['cantidad']} | Precio: {datos['precio']}")
    print("---------------------------")

# 2. Programa Principal con Menu
def ejecutar_sistema():
    """
    Esta función ejecuta el sistema de inventario, mostrando un menú de opciones
    para agregar o actualizar productos, eliminar productos, mostrar el inventario y
    calcular el valor total del inventario, o salir del programa.

    Args:
        None: No toma ningún argumento.
    
    Returns:
        None: No devuelve ningún valor, pero ejecuta el sistema de inventario y maneja la interacción 
        con el usuario a través de la consola.
    """

    inventario_sistema = {}
    
    while True:
        print("SISTEMA DE INVENTARIO")
        print("1. Agregar o actualizar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario y valor total")
        print("4. Salir")
        
        opcion = input("Seleccione una opcion (1-4): ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            # Convertimos las entradas a numeros para poder operar con ellas
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(inventario_sistema, nombre, cantidad, precio)
            
        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(inventario_sistema, nombre)
            
        elif opcion == "3":
            mostrar_inventario(inventario_sistema)
            total = calcular_valor_total(inventario_sistema)
            print(f"Valor total acumulado: {total:.2f}")
            
        elif opcion == "4":
            print("Finalizando programa.")
            break
        else:
            print("Opcion no valida, intente de nuevo.")

# Iniciar el programa
ejecutar_sistema()