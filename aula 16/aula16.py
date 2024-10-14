lanche = ('Hamburguer', 'Suco', 'Batata Frita', 'Pizza', 'Pudim')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')      #MANEIRA 1

 #TUPLAS SAO IMUTAVEIS!!

for comida in lanche:
  print(f'Eu vou comer {comida}')        #MANEIRA 2
print('Comi pra caramba!')

for pos, comida in enumerate(lanche):          #MANEIRA 3 
   print(f'Eu vou comer {comida} na posiçao {pos}')


print(sorted(lanche))   #Colocar os lanches em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a 
print(c)
#print(len(c))
#print(c.count(5)) #Quantas vezes está aparecendo o numero 5 dentro de c
#print(c.index(8)) #Em que posiçao está 8