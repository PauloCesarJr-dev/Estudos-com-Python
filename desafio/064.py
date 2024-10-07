n = 0
cont = 0
soma = 0
while n != 999:
        n = int(input('Digite um numero [999 para parar]: '))
        if n != 999:
            cont += 1
            soma += n  
print('Voce digitou {} numeros e a soma entre eles foi de {}'.format(cont, soma))


# TAMBEM TEM DESSA FORMA

n = 0
cont = 0
soma = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
        n = int(input('Digite um numero [999 para parar]: '))    
        cont += 1
        soma += n 
print('Voce digitou {} numeros e a soma entre eles foi de {}'.format(cont, soma))