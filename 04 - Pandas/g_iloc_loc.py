# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:19 2020

@author: migue
"""


import pandas as pd 

path_guardado = "C:/Users/migue/OneDrive/Documentos/EPN/Sexto Semestre/Desarrollo web con python/Github/py-reina-gamboa-miguel-esteban/04 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

filtrado_horizontal = df.loc[1035] # Serie

print(filtrado_horizontal)

print(filtrado_horizontal['artist'])

print(filtrado_horizontal.index)

serie_vertical = df['artist']

print(serie_vertical)

print(serie_vertical.index)

print(df[['artist']])

# Filtrado por indice

df_1035 = df [df.index == 1035]

segundo = df.loc[1035] #Flitrar por indice (1)
segundo = df.loc[[1035, 1036]] # Filtrar por arr indices
segundo = df.loc[3:5] # Filtrando desdex indice hasta indice
segundo = df.loc[df.index == 1035] #filtrar po arreglo -> T or F
segundo = df.loc[1035, 'artist'] # 1 Indice
segundo = df.loc[1035, ['artist', 'medium']] #Varios indices

#print(df.loc[0]) # Indice dentro del DataFrame
#print(df[0])  #Indice dentro del DataFrame

#iloc -> acceder grupo filas y columnas - indices en 0

tercero = df.iloc[0]
tercero = df.iloc[[0, 1]]
tercero = df.iloc[0: 10]
tercero = df.iloc[df.index == 1035]
tercero = df.iloc[0: 10, 0: 4] # Filtrado indices por rango de indices 0: 4