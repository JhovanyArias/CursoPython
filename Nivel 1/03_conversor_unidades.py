print("Digite la operacion que desea realizar: \n 1. Convertir Metros a Millas \n 2. Convertir Millas a Metros \n 3. Convertir Gramos a Libras \n 4. Convertir Libras a Gramos\n")
tipo_operacion = int(input())
print("Digite la cantidad que desea convertir:")
cantidad = float(input())
if tipo_operacion == 1:
    resultado = round(cantidad/1609,4)
elif tipo_operacion == 2:
    resultado = round(cantidad*1609,4)
elif tipo_operacion == 3:
    resultado = round(cantidad/453.6,4)
elif tipo_operacion == 4:
    resultado = round(cantidad*453.6,4)
else:
    print("Error")

print("El resultado es:",str(resultado))