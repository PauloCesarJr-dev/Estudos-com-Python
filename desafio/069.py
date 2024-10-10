print('-=-'*10)
print('CADASTRE UMA PESSOA')
print('-=-'*10)
tot18 = man = mulher20 = 0 
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': 
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        man += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if tipo == 'N':
        break
    
print(f'Total de pessoas com mais de 18 anos é {tot18}')
print(f'Ao todo temos {man} homen(s) cadastrados.')
print(f'E temos {mulher20} mulhere(s) com menos de 20 anos.')