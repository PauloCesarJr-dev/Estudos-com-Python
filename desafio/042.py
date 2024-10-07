t1 = int(input('Primeiro segmento: '))
t2 = int(input('Segundo segmento: '))
t3 = int(input('Terceiro segmento: '))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os segmentos acima PODEM FORMAR um triangulo', end=' ')
    if t1 == t2 == t3:
        print('EQUILATERO.')
    elif t1 != t2 != t3 != t1:
        print('ESCALENO.') 
    else:
        print('ISOSCELES.')
else:
    print('Os segmentos acima NAO PODEM formar um triangulo.')