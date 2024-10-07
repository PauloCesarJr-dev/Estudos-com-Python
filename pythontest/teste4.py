tot = 0
num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end= ' ')
        tot += 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end= ' ')
print('\nO numero {} foi dividido {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso ele NAO É PRIMO.')