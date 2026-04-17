"""
Este es un programa para la clase de algoritmia y programacion
 de el profesor Juan Pablo Escobar Vargas, el cual se basa en 
 en realizar un programa para un maquina dispensadora, la cual
 permite elegir un rpoducto, ingresar el dinera, entregar el 
 producto y dar la devuelta si es necesario.

Promot: Realiza un programa en python que permita elegir un 
        producto, ingresar el dinero, entregar el producto y 
        dar la devuelta si es necesario.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
17/04/2026

"""
def producto():
    """
    Esta funcion se encarga de mostrar los productos disponibles 
    en la maquina dispensadora, permitir al usuario elegir un 
    producto y devolver el nombre y precio del producto elegido.

    Returns:
        tuple: Una tupla con el nombre y precio del producto elegido.
    """
    productos={ 
        1:["Monster", 9500],
        2:["Chocorramo", 3300],
        3:["Oreo", 2400],
        4:["Agua", 1000],
        5:["Snickers",7100]
        }

    print("productos disponibles: ")
    for nombre, precio in productos.items():
        print(f"{nombre}-{precio}")

    eleccion = int(input("ingrese el numero del producto: "))

    if eleccion == 1:
        return "Monster", 9500
    if eleccion == 2:
        return "Chocorramo", 3300
    if eleccion == 3:
        return "Oreo", 2400
    if eleccion == 4:
        return "Agua", 1000
    if eleccion == 5:
        return "Snickers", 7100
    else:
        print("Opcion no valida.")

def maquina_dispensadora():
    """
    Esta función es para ejecutar el programa central de la 
    maquina dispensadora.

    """
    nombre, precio = producto()

    dinero_ingresado = int(input(f"El precio es {precio}. Ingrese el dinero (billetes/monedas): "))

    if dinero_ingresado < precio:
        print(f"Dinero insuficiente. Falta ${precio-dinero_ingresado}")
        print("Transición fallida.")
        return
        
        
    cambio = dinero_ingresado - precio

    print(f"Producto entregado: {nombre}")

    if cambio > 0:
        print(f"Su devuelta es ${cambio}")
    else:
        print("No hay devuelta.")

    print("¡Gracias por su compra!")

maquina_dispensadora()