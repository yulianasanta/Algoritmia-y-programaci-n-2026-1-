# Si en un reloj digital registra las 6 AM, hacer sonar una alarma por 1 minuto a 
# menos que se accione el botón de apagado.

t= float(input("ingrese el la hora en formato 24h ejemplo(xx,xx): 6.00, 18.00: "))
ti = 0
if t == 6.00:
    print("sonar alarma")
    d = input ("desea apagar alarma? (si/no) ")
    if d == "si":
        print("alarma apagada")
    else:
        print ("sonar alarma")
        for i in range (0, 61):
            print (i)
        if i == 60:
            print ("alarma apagada") 
else:
    print("no sonar alarma")
