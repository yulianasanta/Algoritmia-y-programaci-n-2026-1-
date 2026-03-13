#1. La suma de todos los números pares entre 2 y 100 (ambos inclusive).
# #2. La suma de todos los cuadrados entre 1 y 100 (ambos inclusive).
# #3. La suma de todos los números impares entre a y b (ambos inclusive).
# #4. La suma de todos los dígitos impares de n. (Por ejemplo, si n es 32677, la suma sería 3 + 7 + 7 = 17.)

suma_pares = 0
for i in range (2, 101, 2):
    suma_pares += i
print("la suma de todos los números pares entre 2 y 100 es:", suma_pares)

suma_cuadrados = 0
for i in range (1, 101):
    suma_cuadrados += i**2
print("la suma de todos los cuadrados entre 1 y 100 es:", suma_cuadrados)

suma_impares = 0
a = int(input("ingrese el valor a: "))
b = int(input("ingrese el valor b: "))
for i in range (a, b+1):
    if i % 2 != 0:
        suma_impares += i
print("la suma de todos los números impares entre", a, "y", b, "es:", suma_impares)

n = int(input("ingrese un numero: "))
suma_dig_imp = 0
while n > 0:
    dijito = n % 10
    if dijito % 2 != 0:
        suma_dig_imp += dijito
    n = n // 10
print("la suma de todos los dígitos impares de n es:", suma_dig_imp)
