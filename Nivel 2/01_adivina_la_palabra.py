def encontrar_posiciones(palabra, letra):
    posiciones = []
    for i, char in enumerate(palabra):
        if char == letra:
            posiciones.append(i)
    return posiciones

def reemplazar_en_cadena(cadena, palabra, letra):
    # Obtener las posiciones de la letra en la palabra
    posiciones = encontrar_posiciones(palabra, letra)
    
    # Reemplazar la letra en las posiciones encontradas
    for pos in posiciones:
        cadena[pos] = letra
    return cadena

def juego_adivinanza(palabra):
    # Crear una cadena de 8 espacios en blanco
    cadena = [' '] * 8
    fallos = 0
    
    while ' ' in cadena:
        if fallos >= 5:
            print("El juego ha terminado.")
            break
        
        print("Estado actual:", ''.join(cadena))
        letra = input("Adivina una letra: ")
        
        if letra in palabra:
            cadena = reemplazar_en_cadena(cadena, palabra, letra)
        else:
            fallos += 1
            print("La letra no está en la palabra. Inténtalo de nuevo.\nCantidad de fallos:",fallos)

    if ' ' not in cadena:
        print("¡Felicidades! Adivinaste la palabra:", ''.join(cadena))

# Ejemplo de uso
palabra = "ejemplar"
juego_adivinanza(palabra)