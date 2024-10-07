n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('REPROVADO! Voce teve uma media de {}'.format(media))
elif media < 5.0 or media < 6.9:
    print('RECUPERAÇAO! Voce teve uma media de {} e tera que ir para a recuperaçao!'.format(media))
elif media > 7.0:
    print('PARABENS!, Sua media foi {} e voce está aprovado!'.format(media))
