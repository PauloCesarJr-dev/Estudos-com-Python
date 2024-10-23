print('---'*10)
print('BANCO DO KREEWHAIT')
print('---'*10)
cinquenta = vinte = dez = um = 0
valor = int(input('O Quanto deseja sacar? R$ '))
while valor >= 50:
    cinquenta += 1
    valor -= 50
while valor >= 20:
    vinte += 1
    valor -= 20
while valor >= 10:
    dez += 1
    valor -= 10
while valor >= 1:
    um += 1
    valor -= 1

print(f'Total de {cinquenta} cedulas de R$50 \n Total de {vinte} cedulas de R$20 \n Total de {dez} cedulas de R$10 \n Total de {um} cedulas de R$1')
print('OBRIGADO! VOLTE SEMPRE!')

