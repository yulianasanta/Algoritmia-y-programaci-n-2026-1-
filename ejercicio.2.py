cliente = []
nombre =input ("ingrese su nombre ")
consumo = float (input ("ingrese su consumo en kW/h: "))

if nombre in cliente:
    print (f"El total a pagar es de {consumo*0.15}$")
else:
    cliente.append(nombre)
    print (f"El total a pagar es de {consumo*0.15}$")
    print (cliente)