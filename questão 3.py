numero = int(input("Insira o primeiro número inteiro: "))
numero_2 = int(input("Insira o segundo número inteiro: "))
numero_3 = int(input("Insira o terceiro número inteiro: "))


if numero > numero_2 and numero > numero_3:
    print("O maior número é", numero)
elif numero_2 > numero and numero_2 > numero_3:
    print("O maior número é", numero_2)
else:
    print("O maior número é", numero_3)
