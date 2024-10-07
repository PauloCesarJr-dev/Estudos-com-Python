from math import factorial
num = int(input('Digite um numero para calcular seu Fatorial: '))
resul = factorial(num)
print('Calculando {}! = {}'.format(num, resul))

# DA PRA FAZER ASSIM TAMBEM

num = int(input('Digite um numero para calcular seu fatorial: '))

c = num
f = 1
print('Calculando {}! = '.format(num), end='' )
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
