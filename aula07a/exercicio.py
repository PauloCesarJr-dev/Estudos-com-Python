n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 
e = n1 ** n2 
print('A soma é {}, \n o produto é {} e a \n divisao é {:.3}'.format(s, m, d), end=" ")  # {:.3} (PARA DIMINUIR A QUANTIDADE DE CASAS DECIMAIS!)
print('Divisao inteira {} e potencia {}'.format(di, e))