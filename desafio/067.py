while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
    print('---' * 10)
    for c in range (1, 11):
        print(f'{tabuada} X {c} = {tabuada*c}')
    print('---' * 10)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')
