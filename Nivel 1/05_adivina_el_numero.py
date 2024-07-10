# < >

import random

def adivinar_numero():
    return random.choice(range(10))
numero_sistema = adivinar_numero()

while True:
    print("Digite un numero entre 0 y 9: ")
    numero_usuario = int(input())
    
    if numero_usuario < numero_sistema:
        print ("Mi numero es mayor, intentalo de nuevo - ",numero_sistema)
    elif numero_usuario > numero_sistema:
        print ("Mi numero es menor, intentalo de nuevo - ",numero_sistema)
    elif numero_sistema == numero_usuario:
        print("Adivinaste!")
        break
