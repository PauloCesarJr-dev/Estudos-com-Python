print('==' *10)
print('10 TERMOS DE UMA PA')
print('==' *10)
term1 = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = term1 + (10 - 1) * razao
for c in range(term1, decimo + razao, razao):
    print(c, end=" -> ")
print('Acabou')