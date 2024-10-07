c = 'S'
soma = 0 
totalnum = 0
maior = 0
menor = 0
while c not in "Nn":
    num = int(input('Digite um numero: '))
    c = str(input('Quer continuar? [S/N] ')).strip()
    soma += 1
    totalnum += num
    if soma == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    
media = totalnum / soma
print('Voce digitou {} numeros e a media entre eles é {:.2f}. '.format(soma, media))
print('O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))



