print('---'*10)
print('LOJA SUPER BARATAO')
print('---'*10)
total = prod1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: '))
    cont += 1
    total += preço
    if preço > 1000:
        prod1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    ver = ' '
    while ver not in 'SN':
        ver = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if ver == 'N':
        break

print('---------- FIM DO PROGRAMA -------------')
print(f'O total da compra foi R${total}')
print(f'Temos {prod1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')