# Escribir programas con bucles que calculen
# 1. Todas las potencias de 2 desde 20 hasta 220.
# 2. La suma de todos los números impares comprendidos entre a y b (ambos inclusive), donde a y b son entradas.
# 3. La suma de todos los dígitos impares de una entrada.

for i in range (20, 41):
    print (2**i)
    
a= int(input("ingrese un numero a: "))
b = int(input("ingrese un valor b: "))

n=0
for i in range (a,b):
    if i % 2 != 0:
        n += i
print (n)

b = int(input("ingrese un numero: "))
s=0
while b > 0:
 h = b % 10
 if h % 2 != 0:
    s += h
    b = b // 10
 elif h % 2 == 0:
   print ("el numero", h, "no tiene digitos impares")
   break
print (s)

