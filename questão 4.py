numero = int(input("Insira o primeiro número inteiro: "))
numero_2 = int(input("Insira o segundo número inteiro: "))
numero_3 = int(input("Insira o terceiro número inteiro: "))

maior = 0
menor = 0

if numero > numero_2 and numero > numero_3:
    maior = numero
    if numero_2 > numero_3:
        menor = numero_3
    else:
        menor_numero_2
elif numero_2 > numero and numero_2 > numero_3:
    maior = numero_2
    if numero > numero_3:
        menor = numero_3
    else:
        menor = numero
else:
    maior = numero_3
    if numero_2 > numero:
        menor = numero
    else:
        menor = numero_2

print("O número maior é", maior, "e o número menor é", menor)
