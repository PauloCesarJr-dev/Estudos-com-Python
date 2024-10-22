lista = []
soma = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    soma += 1
    lista.sort(reverse=True)
    resp = ' '
    while resp not in 'SN':
         resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
         break
print('--'*30)
print(f'Voce digitou {soma} elementos.')
print(f'Os valores em ordem decrescente sao {lista}')
if 5 in lista:
         print('O valor 5 faz parte da lista!')
else:
         print('O valor 5 nao faz parte da lista...')

