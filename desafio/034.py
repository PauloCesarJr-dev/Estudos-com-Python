valor = float(input('Qual é o salario do funcionario? R$ '))

if valor <= 900:
    aumento = (0.15 * valor) + valor 
    print('Quem ganhava R${} passa a ganhar R${} agora.'.format(valor, aumento))
if valor > 900:
    aumento2 = (0.10 * valor) + valor
    print('Quem ganhava R${} passa a ganhar R${} agora.'.format(valor, aumento2))