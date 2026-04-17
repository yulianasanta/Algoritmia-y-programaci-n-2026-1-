"""
Este es un programa para la clase de algoritmia y programacion
 de el profesor Juan Pablo Escobar Vargas, El cual se basa en diseñar
 un programa para jugar a adivinar un numero, con diferentes niveles 
 de dificultad, guardando el historial de los resultados en un archivo 
 de texto.

prompt: Realiza un programa en python que permita jugar a adivinar un 
        numero, con diferentes niveles de dificultad, guardando el 
        historial de los resultados en un archivo de texto.

Yuliana Santa Ramírez
c.c. 1089602220
Universidad Tecnologica de Pereira
17/04/2026
"""
#Importamos las librerias necesarias para el programa
import random #Numeros aleatorios
from datetime import datetime #Fecha y hora para el historial

def elegir_deficultad():
    """
    Esta función es para elegir el nivel de dificultad del juego,
    asignando un número de intentos y pistas según la elcción.

    Returns:
        tuple: Una tupla con el número de intentos, pistas y el 
        nombre del nivel.
    """
    print ("nivel de dificultad")
    print("1. Facil (10 intentos, 6 pistas.)")
    print("2. Medio (7 intentos, 4 pistas.)")
    print("3. Dificil (4 intentos, 2 pistas.)")

    opcion =int(input("Elija el nivel de dificultad (1-3): "))

    if opcion == 1:
        return 10, 6, "Facil"
    elif opcion == 2:
        return 7, 4, "Medio"
    elif opcion == 3:
        return 4, 2, "Dificil"
    else:
        print("Opcion no valida. Se asigno nivel medio.")
        return 7, 4, "Medio"


def generar_numero():
    """
    Esta función es para generar un número aleatorio entre 1 y 100.
    
    Returns:
        int: Un número aleatorio entre 1 y 100.
    """
    return random.randint(1,100)


def guardar_archivo(resultado, dificultad):
    """
    Esta función es para guardar el resultado del juego en un archivo de texto,
    incluyendo la fecha y hora, el nivel de dificultad y el resultado.
    Args:
        resultado (str): El resultado del juego.
        dificultad (str): El nivel de dificultad del juego.
    """
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("historial.txt","a") as archivo:
        linea =f"[{fecha_hora} Dificultad: {dificultad}, Resultado: {resultado}]"
        archivo.write(linea)
    print("Resultado guardado en historial.txt")


def jugar(intentos_totales, pistas_totales, nivel_nombre):
    """
    Esta función es para jugar a adivinar un número, utilizando el número de 
    intentos y pistas asignados según el nivel de dificultad elegido.
    Args:
        intentos_totales (int): El número total de intentos.
        pistas_totales (int): El número total de pistas.
        nivel_nombre (str): El nombre del nivel de dificultad.
    """
    numero_secreto=generar_numero()
    intentos_restantes=intentos_totales
    pistas_restantes = pistas_totales

    print (f"He pensado en un numero entre 1 y 100. Tienes {intentos_totales} intentos.")
    print (f"tines {intentos_totales} intentos | tienes {pistas_totales} pistas")
    while intentos_restantes> 0:
        print(f"Intentos restantes: {intentos_restantes}. Pistas restantes: {pistas_restantes}")

        try:
            suposicion = int(input("cual crees que es el numero?:"))
        except ValueError:
            print("Error: Vuelve a intentarlo")
            continue

        if suposicion == numero_secreto:
            mensaje = (f"¡¡Adivinaste el numero!! {numero_secreto}")
            print(mensaje)
            guardar_archivo(mensaje, nivel_nombre)
            return
        
        if pistas_restantes > 0:
            if suposicion < numero_secreto:
                print("Pista: El numero secreto es mayor.")
            else:
                print("Pista: El numero secreto es menor.")
            pistas_restantes -= 1
        else:
            print("Ya no te quedan pistas.")

        intentos_restantes -= 1
        
    perido = f"Perdiste. El numero era {numero_secreto}."
    print(perido)
    guardar_archivo(perido, nivel_nombre)

if __name__ == "__main__":
    jugando = True

    while jugando:
        intentos, pistas, nivel_nombre = elegir_deficultad()
        jugar(intentos, pistas, nivel_nombre)

        if input("¿Jugar de nuevo? (si/no): ") != "si":
            jugando = False
            print("Gracias por jugar.")
