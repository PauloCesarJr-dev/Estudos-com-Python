print('Gerador de PA')
print('-==-' * 5)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
num = 10
while num != 0:
    total = total + num
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')             
    num = int(input('Quantos termos voce quer mostrar mais? '))
print('Progressao finalizada com {} termos mostrados'.format(total))
