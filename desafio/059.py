from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
maiornum = 0
menornum = 0
opçao = 0
while opçao != 5:
      print('''      [ 1 ] Somar
      [ 2 ] Multiplicar
      [ 3 ] Maior
      [ 4 ] Novos numeros
      [ 5 ] Sair do programa ''')
      print('>>>>>>>', end= ' ')
      opçao = int(input('Qual é a sua opçao? '))

      if opçao == 1:
            soma = n1 + n2 
            print('A soma entre {} + {} é {}'.format(n1, n2, soma))
            print('=-=-=' *5)
            sleep(1.7)
      elif opçao == 2:
            multiplicar = n1 * n2
            print('O numero {} x {} é {}'.format(n1, n2, multiplicar))
            print('=-=-' * 5)
            sleep(1.7)
      elif opçao == 3:
            if n1 > n2:
                  maiornum = n1
                  menornum = n2
                  print('O numero {} é maior do que o numero {}.'.format(n1, n2))
                  sleep(1.7)
            if n2 > n1:
                  maiornum = n2
                  menornum = n1
                  print('O numero {} é maior do que o numero {}.'.format(n2, n1))
                  sleep(1.7)
      elif opçao == 4:
            print('Informe os numeros novamente:')
            n1 = int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
      else:
            print('Opçao invalida! Por favor, digite novamente.')
            sleep(1.7)
            
print('Finalizando...')
sleep(1.3)
print('=-=-=-' * 5)
print('Fim do programa, volte sempre!')