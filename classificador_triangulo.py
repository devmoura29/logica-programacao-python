lado_a = int(input("Digite o primeiro lado: "))
lado_b = int(input("Digite o segundo lado: "))
lado_c = int(input("Digite o terceiro lado: "))

if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
   if lado_a == lado_b and lado_b == lado_c:
        print("Equilátero")
   elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
       print("Isósceles")
   else:
       print("Escaleno")

else:
    print("não é um triângulo válido")


