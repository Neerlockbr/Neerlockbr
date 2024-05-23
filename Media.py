n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
n3 = float(input('Digite a Terceira nota: '))
n4 = float(input('Digite a Quarta nota: '))


faltas = int(input('Digite o número de faltas: '))
limite_faltas = int(input('Digite o limite de faltas permitido: '))


m = (n1 + n2 + n3 + n4) / 2


print('A sua média foi {:.1f}'.format(m))


if m >= 6.0:
    if faltas <= limite_faltas:
        print('Sua média foi boa! PARABÉNS!')
    else:
        print('Reprovado por faltas. Faltas: {}, Limite de faltas: {}'.format(faltas, limite_faltas))
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
    if faltas > limite_faltas:
        print('Além disso, você foi reprovado por faltas. Faltas: {}, Limite de faltas: {}'.format(faltas, limite_faltas))


