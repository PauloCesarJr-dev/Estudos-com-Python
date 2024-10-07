mediaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
idademulher = 0
for n in range(1, 5):
    print('----'' {} PESSOA ''----'.format(n))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade 
    if n == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Fm' and idade < 20:
        idademulher += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade)) 
print('O homem mais velho tem {} anos e ele se chamada {}'.format(maioridadehomem, nomevelho))
print('Ao todo sao {} mulher menores do que 20 anos.'.format(idademulher))




