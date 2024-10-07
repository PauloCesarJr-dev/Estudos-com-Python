casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salario do comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestaçao sera de R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Pedido NEGADO!')
