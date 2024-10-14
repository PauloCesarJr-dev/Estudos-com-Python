times = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Sao paulo', 'Internacional', 'Bahia', 'Cruzeiro', 'Atletico Mineiro',
         'Vasco', 'Gremio', 'Criciuma', 'Bragantino', 'Juventude', 'Athletico PR', 'Fluminense', 'Vitoria',
         'Corinthians', 'Cuiaba', 'Atletico goianiense')
print('==='*4)
print(f'Lista de times do Brasileirao: {times}')
print('==='*4)
print(f'Os 5 primeiros sao {times[0:5]}')
print('==='*4)
print(f'Os 4 ultimos sao {times[16:20]}')
print('==='*4)
ordem = sorted(times)
print(f'Times em ordem alfabética: {ordem}')
print('==='*4)
print(f'O Fluminense está na {times.index('Fluminense')} posiçao.')