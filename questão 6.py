numero = int(input("Insira um número: "))
numero_2 = int(input("Insira um número: "))
numero_3 = int(input("Insira um número: "))

reserva = 0

if (numero_2 > numero):
    reserva = numero
    numero = numero_2
    numero_2 = reserva
if (numero_3 > numero_2):
    reserva = numero_2
    numero_2 = numero_3
    numero_3 = reserva
if (numero_2 > numero):
    reserva = numero
    numero = numero_2
    numero_2 = reserva
print(numero, numero_2, numero_3)
