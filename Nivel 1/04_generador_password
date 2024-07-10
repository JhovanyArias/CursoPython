import random

print("Digite la longitud que desea para la contraseña")
longitud=int(input())

def generar_contraseña(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    contraseña = ""

    for _ in range(longitud):
        caracter = random.choice(caracteres)
        contraseña += caracter
    
    return contraseña

contraseña_generada = generar_contraseña(longitud)
print("Contraseña generada:", contraseña_generada)