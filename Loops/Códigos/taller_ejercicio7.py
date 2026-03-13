# Un borracho en una cuadrícula de calles elige al azar una de las cuatro direcciones 
# y tropieza con la siguiente intersección, luego vuelve a elegir al azar una de las 
# cuatro direcciones, y así sucesivamente. Se podría pensar que, por término medio, 
# el borracho no se desplaza mucho porque las elecciones se anulan entre sí, 
# pero en realidad no es así. Representa las ubicaciones como pares enteros (x, y). 
# Implementa el paseo del borracho sobre 100 intersecciones, comenzando en (0, 0), e 
# imprime la ubicación final.


x , y = 0,0

for i in range (0, 5):
    b = int(input("ingrese un numero del 1 al 4 para elegir la direccion del borracho: "))
    if b == 1:
        x= x+1
    elif b == 2:
        x = x-1
    elif b == 3:
        y = y+1
    elif b == 4:
        y = y-1
    if i == 5:
        break 
print(f"el borracho esta en {x},{y}")
        
        
