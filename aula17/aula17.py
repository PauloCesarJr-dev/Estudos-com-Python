#lanche.append('cookie') - adicionar no final
#lanche.insert(0,'cookie') - adicionar no meio dependendo da posiçao (0,1,2,3)

            #REMOVER DA LISTA
#del lanche[3]
#lanche.pop(3)
#lanche.remove('cookie')  -> se deixar apenas () ele vai eliminar o ultimo elemento

#if 'pizza' in lanche:
     #lanche.remove('pizza')

#valores=list(range(4,11))

#valores.sort()  -> organizar os valores
#valores.sort(reverse=True) -> ordem reversa

''''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Nao achei o numero 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posiçao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

''''a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
