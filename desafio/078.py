valores = [int(input('Digite um valor para a Posiçao 0: ')), int(input('Digite um valor para a Posiçao 1: ')),
           int(input('Digite um valor para a Posiçao 2: ')), int(input('Digite um valor para a Posiçao 3: ')),
           int(input('Digite um valor para a Posiçao 4: '))]
print('='*40)
print(f'Voce digitou os valores {valores} ')
print(f'O maior valor digitado foi {max(valores)} nas posiçoes', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f' {i}...', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posiçoes', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f' {i}...', end='')


    

    