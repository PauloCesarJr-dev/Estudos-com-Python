from random import randint
pc = randint(0, 10)
tottentativas = 1
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Será que voce consegue adivinhar qual foi?')
jogador = int(input('Qual é seu palpite? '))
while not pc == jogador:
    jogador = int(input('Qual é o seu palpite? '))
    tottentativas += 1
    if pc != jogador:
        if jogador > pc:
            print('Menos...Tente mais uma vez.')
        else:
            print('Mais...Tente mais uma vez.')     
if jogador == pc:
     print('Acertou com {} tentativa(s). Parabens!'.format(tottentativas))


# OU ESSA FORMA

from random import randint
pc = randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Será que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if pc == jogador:
        acertou = True
    else:
        if jogador > pc:
            print('Menos...tente mais uma vez')
        elif jogador < pc:
            print('Mais... tente mais uma vez')   
print('Acertou em {} tentativas. Parabens!'.format(palpites))
