peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO DO PESO normal.')
if 18.5 <= imc < 25:
    print('Voce está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Voce está ACIMA DO PESO IDEAL.')
elif 30 <= imc < 40:
    print('Voce está em OBESIDADE!')
else:
    print('Voce está em OBESIDADE MORBIDA, cuidado!')

