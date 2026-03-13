# Escriba un programa que pida al usuario un número entero y luego imprima todos sus 
# factores. Por ejemplo, cuando el usuario introduce 150, el programa debe imprimir:
# 2
# 3
# 5
# 5

d =int(input("ingrese un numero entero: "))
n = 2

for i in range (1 , d+1):
 if d % n == 0:
    d = d//n
    print (n)
 else:
    n = n + 1
 
