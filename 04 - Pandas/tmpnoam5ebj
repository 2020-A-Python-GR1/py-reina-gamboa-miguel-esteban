# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:32:41 2020

@author: migue
"""

# f_indices_filtrado.py

import pandas as pd

path_guardado = "C:/Users/migue/OneDrive/Documentos/EPN/Sexto Semestre/Desarrollo web con python/Github/py-reina-gamboa-miguel-esteban/04 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(type(artistas))  # numpy array

print(artistas.size)

print(len(artistas))

blake = df ['artist'] == 'Blake, William' # Serie

print(blake.value_counts())

df_blake = df[blake] #DataFrame