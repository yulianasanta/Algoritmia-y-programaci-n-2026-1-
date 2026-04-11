# Factorial (n)
"""
En este código es para calcular el factorial de caulquier número n, 
el cual se define como el producto de todos los enteros desde 1 hasta n.

Prompt: Hola, puedes hacerme un código de phyton para una serie n de
        factorial.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
fecha:
"""
def factorial(n):
    """
    Esta funcion es para calcular el factorial de caulquier número 
    entero no negativo.

    Args:
        n(int): El numero del cual se desea obtener el factorial.

    Returns:
        int: Es el resultdo del factorial en la posición n.
    """
    if n==1 or n==0: 
        """El if se utilizo para el caso base el cual dice que el
        factorial de 0 ó 1 es 1"""
        return 1
        #Recursividad
    else:
        return n*(factorial(n-1))
"""retorna a n y lo multiplica por por el numero anterior"""
    
print(factorial(4))