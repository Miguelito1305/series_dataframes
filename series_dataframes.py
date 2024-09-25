import pandas as pd
psg_players = pd.Series(
    ['navas', 'mbappe', 'neymar', 'messi', 'ronaldo'],
    index=[1, 7, 10, 30, 40]
)
psg_dict = {1: 'navas', 7: 'mbappe', 10: 'neymar', 30: 'messi', 40: 'ronaldo'}
psg_players_dict = pd.Series(psg_dict)
#print(psg_players)
print(psg_players_dict)
print(psg_players[7])
print(psg_players_dict[0:3])
#Diccionario con datos de jugadores
dict = {'Jugador': ['Navas', 'Mbappe', 'Neymar', 'Messi'], 
        'Altura': [183.0, 170.0, 170.0, 165.0], 
        'Goles': [2, 200, 150, 200]}
#Crear un dataframe con el diccionario e índices personalizado
df = pd.DataFrame(dict, index=[1,7,10,30])
print(df)