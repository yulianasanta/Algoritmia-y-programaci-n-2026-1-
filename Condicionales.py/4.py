# medidor_humedad_1: es el sensor de arriba del tanque
# medidor_humedad_2: es el sensor de abajo del tanque
medidor_humedad_1 = int (input("ingrese el valor de humedad en 1. "))
medidor_humedad_2 = int (input ("ingrse el valor de humedad en 2. "))

if medidor_humedad_2 == 0:
    print ("activar bomba de agua")
    print ("tanque vacio")
elif medidor_humedad_1 == 1:
    print ("desactivar bomba de agua")
    print ("tanque lleno")

if medidor_humedad_1 == 0 and medidor_humedad_2 == 1:
    print ("tanque medio lleno")