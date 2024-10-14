numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
         'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 
        'Dez', 'Onze', 'Doze', 'Treze',
        'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
         'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. Digite um número entre 0 e 20: ')
print(f'Voce digitou o numero {numeros[num]}')


    


    



