peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Abaixo do peso")
elif imc >=18.5 and imc <=24.9:
    print("Peso normal")
elif imc >=25 and imc <=29.9:
    print("Sobrepeso")
elif imc >=30 and imc <=34.9:
    print("Obesidade grau 1")
elif imc >=35 and imc <=39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")

    

