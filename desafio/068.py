from random import randint
print('=-='*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-='*10)
v = 0
tipo = ' '
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)
    soma = jogador + pc 
    while tipo not in "PI":    
        tipo = str(input('Par ou impar?[P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {pc}. Total de {soma}', end='')
    print('DEU PAR!' if soma % 2 == 0 else 'DEU IMPAR')
    if tipo == "P":
        if soma % 2 == 0:
            print('Voce venceu!!')
            v += 1
        else:
            print('Voce perdeu!!')
            break
    elif tipo == "I":
        if soma % 2 == 1:
            print('Voce venceu!!')
            v += 1
        else:
            print('Voce perdeu!!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')





        
