for c in range(1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM!')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')


par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: #para poder o 0 nao somar como um numero par
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares!'.format(par, impar))