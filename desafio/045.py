from random import randint
from time import sleep
print('''Suas opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input(('Qual é a sua jogada? ')))
pc = randint(0, 2) 
itens = ('Pedra', 'Papel', 'Tesoura')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if jogador == 0 and pc == 2 or jogador == 2 and pc == 1 or jogador == 1 and pc == 0:
    print('===================================')
    print('Computador jogou {}'.format(itens[pc]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('===================================')
    print('\032[33mJOGADOR VENCE')
elif pc == 0 and jogador == 2 or pc == 2 and jogador == 1 or pc == 1 and jogador == 0:
    print('===================================')
    print('Computador jogou {}'.format(itens[pc]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('===================================')
    print('\033[31mCOMPUTADOR VENCE')
elif pc == jogador or jogador == pc:
    print('===================================')
    print('Computador jogou {}'.format(itens[pc]))
    print('Jogador jogou {}'.format(itens[pc]))
    print('EMPATE!')
else:
    print('NÚMERO INVALIDO, Digite novamente!')

