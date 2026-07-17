idade = int(input("Digite a idade: "))

if idade < 16:
    print("Não pode votar")
elif idade >= 16 and idade < 18:
    print("Voto opcional")
elif idade >= 18 and idade <= 69:
    print("Voto obrigatório")
else:
    print("Voto opcional")
