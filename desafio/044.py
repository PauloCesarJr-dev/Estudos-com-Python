print('=================== LOJAS GUANABARA =====================')
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
      [1] à vista dinheiro/cheque
      [2] à vista cartao
      [3] 2x no cartao
      [4] 3x ou mais no cartao''')
opçao = int(input('Qual é a opçao? '))
vista = preço - (preço * 10 / 100)
cartao = preço - (preço * 5 / 100)
dcartao = preço / 2

if opçao == 1:
    print('Sua compra de R${} vai custar R${} no final.'.format(preço, vista))
elif opçao == 2:
    print('Sua compra de R${} vai custar R${} no final.'.format(preço, cartao))
elif opçao == 3: 
    print('Sua compra de R${} vai ser parcelado em 2x numa quantia de R${} em dois meses.'.format(preço, dcartao))
elif opçao == 4:
    parcela = int(input('Quantas parcelas? '))
    juros = preço + (preço * 20 / 100)
    parce = juros / parcela 
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, parce))
    print('Sua compra de R${} vai custar R${:.2f} no final.'.format(preço, juros))
else: 
    print('[ERRO] Digite novamente o número.')

