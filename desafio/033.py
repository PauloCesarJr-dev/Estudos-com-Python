v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
lista = [v1, v2, v3]
print('O menor valor digitado foi {}'.format(min(lista)))
print('O maior valor digitado foi {}'.format(max(lista)))

# DA PRA FAZER DESSE JEITO AQUI TBM:

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#verificando menor
menor = a
if b < a and b < c:
    menor = b 
if c < a and c < b:
    menor = c 
#verificando maior
maior = a  
if b > b and b > c:
    maior = b 
if c > a and c > b:
    maior = c 
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
    
