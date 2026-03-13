# Un tanque de agua tiene dos detectores: uno de tanque lleno y otro de tanque vacío. 
# Una persona extrae continuamente agua del tanque. 
# Un sistema automático abre la válvula de entrada de agua si el detector de tanque vacío 
# se activa. La válvula permanece abierta hasta que el detector de tanque lleno se activa. 
# En ese momento se debe cerrar la válvula.

h1= int(input("Valor humedad 1: ")) #sensor arriba del tanque
h2 = int(input("valor humedad 2: ")) #sensor abajo del tanque
b = 0  # válvula cerrada

while True:
    if h2 == 0:
        print ("tanque vacio2")
    b =+ 1
    if h1 == 1:
        print ("tanque lleno")
        b =- 1
    break
else: h2 == 1 and h1 == 0
print  ("tanque medio lleno")