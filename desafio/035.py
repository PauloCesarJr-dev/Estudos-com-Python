print('-==-' * 10)
print('Analisador de Triangulos')
print('-==-' * 10)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um tringulo') 
else:
    print('Os segmentos acima NAO PODEM formar um triangulo')
