#v1

print("Digite un numero: ")
numero_uno  = int(input())
print("Digite otro numero: ")
numero_dos = int(input())
print("Digite la operacion que desea realizar: \n 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. Division")
tipo_operacion = int(input())
resultado = 0
if tipo_operacion == 1:
    resultado = numero_uno + numero_dos
elif tipo_operacion == 2:
    resultado = numero_uno - numero_dos
elif tipo_operacion == 3:
    resultado = numero_uno * numero_dos
elif tipo_operacion == 4:
    resultado = numero_uno / numero_dos
else:
    print("Error")
print("El resultado es:",str(resultado))





# v2

numero_uno  = int(input("Digite un numero: "))
numero_dos = int(input("Digite otro numero: "))
tipo_operacion= input("Digite la operacion que desea realizar: (+ - * /)")
match tipo_operacion:
    case "+":
        resultado=numero_uno+numero_dos
    case "-":
        resultado=numero_uno-numero_dos
    case "*":
        resultado=numero_uno*numero_dos
    case "/":
        resultado=numero_uno/numero_dos
print(f"El resultado de {numero_uno} {tipo_operacion} {numero_dos} es igual a {resultado}") 
#prin(f"Hola"{numero_dos}) 
# Permite concatenar variables entre llaves dentro del print