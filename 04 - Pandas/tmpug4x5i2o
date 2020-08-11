# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:18:45 2020

@author: migue
"""


import pandas as pd
import os
path = "C:/Users/migue/OneDrive/Documentos/EPN/Sexto Semestre/Desarrollo web con python/Github/py-reina-gamboa-miguel-esteban/04 - Pandas/data/artwork_data.csv"

df1 = pd.read_csv(
    path,
    nrows = 10)

columnas = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

df2 = pd.read_csv (
    path,
    nrows = 10,
    usecols = columnas)

df3 = pd.read_csv (
    path,
    usecols = columnas,
    index_col = 'id',
    low_memory = False)

path_guardado = "C:/Users/migue/OneDrive/Documentos/EPN/Sexto Semestre/Desarrollo web con python/Github/py-reina-gamboa-miguel-esteban/04 - Pandas/data/artwork_data.pickle"

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)
