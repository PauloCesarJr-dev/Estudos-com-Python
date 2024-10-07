from datetime import date 
atual = date.today().year
data = int(input('Ano de nascimento: '))
idade = atual - data
if data <= 9:
    print('Voce tem {} anos, portanto, categoria MIRIM.'.format(idade))
elif data <= 14:
    print('Voce tem {} anos, portanto, categoria INFANTIL.'.format(idade))
elif data <= 19:
    print('Voce tem {} anos, portanto, categoria JUNIOR.'.format(idade))   
elif data <= 25:
    print('Voce tem {} anos, portanto, categoria SENIOR.'.format(idade)) 
else:
    print('Voce tem {} anos, portanto, categoria MASTER.'.format(idade))
