("lanzar el dado")
caras_dado = int(input("ingrese el número del dado: "))
X = 0
Y = 0
tiros = 0

if caras_dado == 1:
    ficha = X+1,Y
    tiros = tiros + 1
    print (f"la ficha se mueve a {ficha}")
    print (f"tiros: {tiros}")
if caras_dado == 2:
    ficha = X,Y-1
    tiros = tiros + 1
    print (f"la ficha se mueve a {ficha}")
    print (f"tiros: {tiros}")
if caras_dado == 3:
    ficha = (X-1,Y)
    tiros = tiros + 1
    print (f"la ficha se mueve a {ficha}")
    print (f"tiros: {tiros}")
if caras_dado == 4:
    ficha = (X,Y+1)
    tiros = tiros + 1
    print (f"la ficha se mueve a {ficha}")
    print (f"tiros: {tiros}")
if caras_dado != 1 and caras_dado != 2 and caras_dado != 3 and caras_dado != 4:
    print ("Cara no válida")
if tiros == 10:
    print (f"la posición final de la ficha es {ficha}")
