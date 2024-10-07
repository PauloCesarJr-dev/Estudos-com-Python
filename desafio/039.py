from datetime import date
genero = str(input('Qual é o seu genero? '))
data = int(input('Ano de nascimento: '))
nascimento = date.today().year
idade = nascimento - data 
print('Quem nasceu em {} tem {} anos em {}.'.format(data, idade, nascimento))

if genero == 'mulher':
    print('Voce nao precisa fazer o serviço militar obrigatorio.')

elif idade == 18:
    saldo = 18 - idade 
    print('Voce tem que se alistar imediatamente!')
    ano = nascimento + saldo
elif idade < 18:
    saldo = idade - 18
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = nascimento - saldo 
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado há {} anos'.format(saldo))
    ano = nascimento - saldo
    print('Seu alistamento foi em {}.'.format(ano)) 





