n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
m = (n1 + n2) / 2
print('Sua média é {}'.format(m))
if m >= 6.0:
    print("PARABENS! Sua média é boa!")
else: 
    print('ESTUDE MAIS! Sua média foi ruim!')