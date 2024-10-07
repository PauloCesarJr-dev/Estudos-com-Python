sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, por favor, Digite seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))


    
       
