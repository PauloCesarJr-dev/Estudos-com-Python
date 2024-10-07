nomevelho = ''
maioridadehomem = 0
mediaidade = 0
somaidade = 0
idademulher20 = 0
for p in range(1, 5):
    print('---- {} PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade 
        nomevelho = nome 
    if sexo in 'Ff' and idade < 20:
        idademulher20 += 1
mediaidade = somaidade / 4
print('A idade media do grupo é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos.'.format(idademulher20))

