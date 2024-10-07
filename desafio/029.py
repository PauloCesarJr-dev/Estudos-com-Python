radar = float(input('Qual é a velocidade atual do carro? '))
multa = (radar - 80) * 7
if radar <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Voce excedeu o limite permitido que é de 80Km/h\nVoce deve pagar uma multa de R${}'.format(multa))