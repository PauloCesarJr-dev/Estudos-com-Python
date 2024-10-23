from time import sleep
print('=='*40)
print('Hmmmmm....vamos verificar se voce é o amor da minha vida ou algum impostor...')
print('=='*40)

nome = str(input('Digite seu primeiro nome: ')).upper().strip()
if nome == 'ADRIELLE':
    sleep(1.5)
    print(f'{nome} sei....ainda tenho minhas duvidas...')
    sleep(1.5)
    cod = int(input('Se voce é mesmo quem voce diz que é...qual é o nosso codigo secreto? '))
    if cod == 143:
        sleep(1.5)
        print('Hummmm...')
        sleep(1.5)
        print('❤️ ❤️ ❤️ ❤️  É o amor da minha vida mesmo!! ❤️ ❤️')
        sleep(1.5)
        print('❤️ ❤️ ❤️ ❤️  EU TE AMO MIL MILHOES! ❤️ ❤️ ❤️ ❤️')
    else:
        print('EU SABIA!!! Voce nao é a minha princesa, saia daqui agora!')
else:
    print(f'Saia daqui, {nome} seu(a) impostor(a) imundo(a), esse lugar nao é pra voce!')

jogo = ' '
while jogo not in 'SN':
    jogo = str(input('Vamos brincar mais um pouco? [S/N] ')).strip().upper()
    if jogo == 'N':
        break
    

