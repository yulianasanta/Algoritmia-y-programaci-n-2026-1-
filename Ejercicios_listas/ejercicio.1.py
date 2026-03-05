# Una empresa de energía quiere llevar un registro de sus clientes y su consumo de energía. 
# Se pide realizar un programa que permita ingresar el nombre del  cliente y su consumo en kWh, 
# y luego calcular el costo total a pagar considerando que el precio por kWh es de $0.15.

lista = ["juan", "pablo", "maria", "hector", "luisa"]
nombre = input ("ingrese su nombre en minuscula:")

if nombre in lista:
    print ("Hola")
else:
    lista.append (nombre)
    print ("nombre agregado a la lista")
    print (lista)
