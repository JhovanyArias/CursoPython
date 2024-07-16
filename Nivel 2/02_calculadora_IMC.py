peso=float(input("Digite su peso"))
talla=float(input("Digite su altura en metros"))
IMC=0
IMC = peso/(talla**2)
if IMC < 18.5:
    print("Bajo Peso")
elif 18.5 <= IMC <= 24.9:
    print("Peso Normal")
elif 25 <= IMC <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")