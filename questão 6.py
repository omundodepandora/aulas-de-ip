numero = int(input("Insira um número: "))
numero_2 = int(input("Insira um número: "))
numero_3 = int(input("Insira um número: "))

reserva = 0

if numero_2 > numero and numero_2 > numero_3:
    reserva = numero
    numero = numero_2
    numero_2 = reserva
    if numero_3 < numero_2:
        reserva = numero_2
        numero_2 = numero_3
        numero_3 = reserva
    else:
        numero_2 = numero_2
        numero_3 = numero_3
if numero_3 > numero and numero_3 > numero_2:
    reserva = numero
    numero = numero_3
    numero_3 = reserva
    print(numero, numero_2, numero_3)
    if numero_2 < numero_3:
        reserva = numero_2
        numero_2 = numero_3
        numero_3 = reserva
    else:
        numero_2 = numero_2
        numero_3 = numero_3
else:
    numero = numero
    if numero_3 < numero_2:
        numero_2 = numero_2
        numero_3 = numero_3  
    else:
        reserva = numero_2
        numero_2 = numero_3
        numero_3 = reserva

print(numero, numero_2, numero_3)
