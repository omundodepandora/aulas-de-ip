nota = float(input("Insira a primeira nota do aluno: "))
nota_2 = float(input("Insira a segunda nota do aluno: "))

media = (nota + nota_2)/2

if media >= 7.0:
    print("Aprovado por média")
elif media >= 4.0 and media < 7.0:
    print("Necessita realizar exame final")
else:
    print("Reprovado por média")
    
