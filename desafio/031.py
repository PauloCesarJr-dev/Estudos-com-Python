distancia = float(input('Qual a distancia da viagem? '))
passagem = distancia * 0.50 
passagem2 = distancia * 0.45
print('Voce está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia >= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(passagem2))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(passagem))


    # OU PODEMOS FAZER ASSIM

distancia = float(input('Qual é a distancia da sua viagem? '))
print("Voce está prestes a começar uma viagem de {}Km.".format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print("E o preço da sua passagem será de R${}".format(preço))