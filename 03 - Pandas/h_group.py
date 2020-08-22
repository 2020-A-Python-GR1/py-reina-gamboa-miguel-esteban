# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:55:54 2020

@author: migue
"""


import numpy as np
import pandas as pd
import math

path_guardado = "C:/Users/migue/OneDrive/Documentos/EPN/Sexto Semestre/Desarrollo web con python/Github/py-reina-gamboa-miguel-esteban/04 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)
seccion_df = df.iloc[49980:50019, :].copy()

df_agrupar_artist = seccion_df.groupby('artist')
print(type(df_agrupar_artist))

for columna, df_agrupado in df_agrupar_artist:
    print(type(columna))
    print(columna)
    print(type(df_agrupado))
    print(df_agrupado)
    
# Hacer calculos en las columnas del df
    
a = seccion_df['units'].value_counts()
#38mm
#1NoN

#Verificar si la comuna está vacia
print(a.empty)

def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    #Si está vacio no hacemos nada
    if(lista_valores.empty):
        return series
    else:
        if(tipo == 'promdeio' ):
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                if(isinstance(valor_serie, str)):
                    valor = int(valor_serie)
                    numero_valores = numero_valores + 1
                    suma = suma + valor
                else:
                    pass
            promedio = suma / numero_valores
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
        if(tipo == 'mas_repetido' ):
            mas_repetido = series.value_counts().idmax()
            series_valores_llenos = series.fillna(mas_repetido)
            return series_valores_llenos
        
def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df=[]
    for artista, df in df_artist:
        copia_df = df.copy()
        serie_w = copia_df['width']
        serie_h = copia_df['height']
        serie_u = copia_df['units']
        serie_i = copia_df['inscription']
        copia_df.loc[:, 'width'] = llenar_valores_vacios(
            serie_w,
            'promedio'
            )
    