numero = int(input("Insira o primeiro número inteiro: "))
numero_2 = int(input("Insira o segundo número inteiro: "))

print("num1 =", numero, "num2 =", numero_2)
reserva = 0

reserva = numero_2
numero_2 = numero
numero = reserva

print("num1 =", numero, "num2 =", numero_2)
