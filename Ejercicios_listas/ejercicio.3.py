inventario ={"producto": "precio",
      "manzana":"2.5",
      "banana":"1.8",
      "naranja":"3.0",
      "pera" : "2.0",
      "monster" : "5.0",
      "agua":"1.0",
      "coca-cola":"3.5"}

producto = input("Ingrese el producto: " )
precio = input ("Ingrese el precio del producto: ")

if producto in inventario:
    print ("El producto esta en el inventario")
    eliminar_producto= input ("Desea eliminar el producto: (si/no) ")
    if eliminar_producto == "si":
        inventario.pop(producto)
        print (f"El producto {producto} se elimino del inventario")
        print (inventario)
    else:
        cambiar_precio = input ("Desea cambiar el precio del producto? (si/no): ")
        if cambiar_precio == "si":
            nuevo_precio =input ("Ingrese el nuevo precio del producto: ")
            inventario[producto] = nuevo_precio
            print (f"Se actualizo el precio del producto {producto} a {nuevo_precio}")
            print (inventario)
elif producto not in inventario:
    print ("El producto no esta en el inventario")
    agregar_producto = input ("Desea agregar el producto al inventario? (si/no): ")
    if agregar_producto == "si":
        inventario[producto] = precio
        print (f"El producto {producto} se agrego al inventario con el precio de {inventario[producto]}")
        print (inventario)
    else:
        print ("No se agrego el producto al inventario")
        print (inventario)