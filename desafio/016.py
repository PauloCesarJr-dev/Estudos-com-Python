from math import trunc
num = float(input('Digite um numero: '))
inteiro = trunc(num)
print('O numero {} tem a parte inteira {}.'.format(num, inteiro))

# PODEMOS FAZER DESSE JEITO TAMBEM:
# num = float(input('Digite um numero: '))
# print('O valor digitado foi {} e a sua porçao inteira é {}'.format(num, int(num)))