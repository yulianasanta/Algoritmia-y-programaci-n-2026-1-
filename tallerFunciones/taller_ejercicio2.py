"""
En este ejercicio se va a realizo un código para aplicar conceptos adquiridos en clase
de funciones para realizar operaciones matemáticas en este caso se raalizaron las 
operaciones de suma, resta, multiplicación, división, raiz cuadrada, exponente, factorial
e inversa.

prompt: realiza un programa para python que realice la raíz cuadrada,
        exponente y factorial de un numero.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
15/04/2026
"""
def suma (a=0,b=0):
    """
    Esta funcion es para calcular la suma de dos varaibles "a" y "b".

    Args:
        a (float): El primer número a hacer la operación.
        b (float): El segundo número para hacer la operación.
    
    Returns:
        float: La suma de los dos números.
    """
    return a + b
def resta (a=0,b=0):
    """
    Esta es la función para calcular la resta de las dos variables
    "a" y "b"

    Args:
        a (float): El primer número a hacer la operación.
        b (float): El segundo número para hacer la operación.

    Returns:
        float: La resta de los dos números.
    """
    return a - b
def multiplicacion (a=0,b=0):
    """
    Esta función es para calcular la multiplicación de las dos variables

    Args:
        a (float): El primer número a hacer la operación.
        b (float): El segundo número para hacer la operación.
    Returns:
        float: La multiplicación de los dos números.
    """
    return a * b
def division (a=0,b=0):
    """
    Esta función es para calcular la división de las dos variables.

    Args:
        a (float): El primer número a hacer la operación.
        b (float): El segundo número para hacer la operación.

    Returns:
        float: La división de los dos números.
        Error: Si el segundo número es cero, devuelve un mensaje de error.
    """
    # Verifica si el divisor es cero y si es así imprimir el error
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def exponente (a=0,b=0):
    """
    Calcula base^exponente usando multiplicaciones 

    Args:
        a (float):  Es el número que se desea elevar.
        b (float): Es el número de cauntas veses se va a multiplicar.

    Returns:
        float: La potencia de la base elevada al exponente.
    """
    # Si b=0 retornar 1, ya que cualquier número elevado a la potencia de 0 es igual a 1.
    if b==0:
        return 1
    resultado = 1

    # Se va moviendo el por cada iteración multiplicando el resultado por la base "a" y se repite esto "b" veces.
    for i in range(b):
        resultado = multiplicacion(resultado, a)
    return resultado if b > 0 else (1, resultado)

def raiz_cuadrada (a):
    """
    Esta función es para calcular la raíz cuadrada de un número.

    Args:
        a (float): El número del cual se desea calcular la raíz cuadrada.

    Returns:
        float: La raíz cuadrada del número.
        Error: Si el número es negativo, devuelve un mensaje de error.
    """
    #Si a es un numero negativo retorna Error.
    if a<0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    return a ** 0.5

def factorial (a):
    """
    Esta función es para calcular el factorial de un número.

    Args:
        a (float): El número del cual se desea calcular el factorial.

    Returns:
        float: El factorial del número "a".
        Error: Si el número es negativo, devuelve un mensaje de error.
    """
    if a<0:
        return "Error: No se puede calcular el factorial de un número negativo."
    #si a es 0 o 1, el factorial es 1, ya que 0! y 1! son iguales a 1.
    elif a==0 or a==1:
        return 1
    
    else:
        resultado = 1
        for i in range(2, a+1):
            resultado *= i
        return resultado 
    
def inversa (a):
    """
    Esta función es para calcular la inversa de un número.
    Args:
        a (float): El número del cual se desea calcular la inversa.
    Returns:
        float: La inversa del número.
        Error: Si el número es cero, devuelve un mensaje de error.
    """

    if a==0:
        return "Error: No se puede calcular la inversa de cero."
    return 1/a

def operacion(z):
    """
    Define una función que toma un número entero "z" como argumento 
    y realiza una operación matemática específica según el valor de "z".

    Args:
        z (int): El número que indica la operación a realizar (1-8).

    Returns:
        float: El resultado de la operación matemática específica.
    """
    if z == 1:
        return suma(a, b)
    elif z == 2:
        return resta(a, b)
    elif z == 3:
        return multiplicacion(a, b)
    elif z == 4:
        return division(a, b)
    elif z == 5:
        return exponente(a, b)
    elif z == 6:
        return raiz_cuadrada(a)
    elif z == 7:
        return factorial(a)
    elif z == 8:
        return inversa(a)
    else:
        return "Error: Opción no válida. Por favor, elija un número del 1 al 8."

z = int(input("Ingrese el número de la operación que desea realizar (1-8): "))
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultado = operacion(z)
print("El resultado de la operación es:", resultado)