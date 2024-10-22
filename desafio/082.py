lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)     
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista com numeros pares é {listap}')
print(f'A lista de impares é {listai}')
    
    

