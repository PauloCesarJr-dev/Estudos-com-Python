numero = int(input('Me diga um numero: '))
resultado = numero % 2 
if resultado == 0:
    print('O numero digitado foi {} e ele é um Numero PAR'.format(numero))
else:
    print('O numero digitado foi {} e ele é um Numero IMPAR'.format(numero))