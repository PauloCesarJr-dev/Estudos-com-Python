num = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), 
       int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')),)
print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 está na posiçao {num.index(3)+1}')
else:
    print('O valor 3 nao foi digitado em nenhuma posiçao')
for n in num:
    if n % 2 == 0:
        print(f'Os numeros pares foram {n}')