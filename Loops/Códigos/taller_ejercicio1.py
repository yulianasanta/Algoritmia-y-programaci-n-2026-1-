# Escriba un bucle while que imprima:
# 1. Todos los cuadrados menores que n. Por ejemplo, si el usuario ingresa n igual a 100, imprime 0 1 4 9 16 25 36 49 64 81.
# 2. Todos los números positivos que son divisibles por 10 y menores que n. Por ejemplo, si el usuario ingresa un valor de 100, imprimiría 10 20 30 40 50 60 70 80 90
# 3. Todas las potencias de dos menores (2**contador) que n. Por ejemplo, si el usuario ingresa un
# valor de n igual a 100, imprime 1 2 4 8 16 32 64.

n = int(input("ingrese un numero: "))
i = 0
while i*i < n:
    print(i*i)
    i += 1

for i in range (10, n, 10):
    print(i)
    
p = 1
while p < n:
    print(p)
    p = p * 2
