metros = float(input('Digite em metros: '))

cent = metros * 100
mili = metros * 1000
km = metros * 0.001

print('{} metros é igual a {:.0f} centimetros'.format(metros, cent))
print('{} metros é igual a {:.0f} milimetros'.format(metros, mili))
print('{} Metros equivale a {} kilometros'.format(metros, km))