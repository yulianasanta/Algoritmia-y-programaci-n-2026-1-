reloj= float (input ("ingrse la hora en fromato 24 horas, ejemplo (xx.xx): 6.00,15.00. "))
if reloj == 6.00:
    print ("sonar alarma")
    boton = int(input ("apagar alarma? "))
    if boton == 1:
        print ("alarma apagada")
    elif boton == 0:
        print ("Sonar por un minuto más")
else: print("no sonar alarma")


