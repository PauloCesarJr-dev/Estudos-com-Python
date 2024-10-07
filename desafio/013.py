sal = float(input('Qual é o salario do funcionario? R$ '))
aum = sal + (sal * 15 / 100)
print('Um funcionario que ganhava R${}, com 15% de aumento, passa a receber R${:.2f} '.format(sal, aum))