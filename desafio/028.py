from random import randint
from time import sleep
pc = randint(0, 5) # Faz o computador ''pensar''
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3) # METODO PARA FAZER O PC "DORMIR" POR ALGUNS SEGUNDOS
if jogador == pc:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print("PERDEU! Eu pensei no numero {} e nao no {}!".format(pc, jogador))



