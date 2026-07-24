
categoria = input("Qual a categoria (vip ou comum)?")
while categoria != "vip" and categoria != "comum":
    categoria = input("Categoria inválida. Digite vip ou comum: ")
compra = float(input("Qual o valor da compra? "))
if categoria == "vip":
    if compra > 200:
        valor_final = compra - (compra * 0.20)
        print(f" Você teve 20% de desconto e vai pagar R$ {valor_final}")
    else:
        valor_final = compra - (compra * 0.10)
        print(f"você teve 10% de desconto e vai pagar R$ {valor_final}")
elif categoria == "comum":
    if compra > 500:
        valor_final = compra - (compra * 0.10)
        print(f"você teve 10% de desconto e vai pagar R$ {valor_final}")
    else:
        valor_final = compra
        print(f"sua compra saiu no valor R$ {valor_final}")