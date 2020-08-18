# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:05:11 2020

@author: migue
"""


import pandas as pd
import numpy as np
import xlsxwriter


path_guardado = "C:/Users/migue/OneDrive/Documentos/EPN/Sexto Semestre/Desarrollo web con python/Github/py-reina-gamboa-miguel-esteban/04 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

data = sub_df['artist'].value_counts()

rango_celdas = 'B2:B{}'.format(len(data.index)+1)

cuaderno = xlsxwriter.Workbook("C:/Users/migue/OneDrive/Documentos/EPN/Sexto Semestre/Desarrollo web con python/Github/py-reina-gamboa-miguel-esteban/04 - Pandas/data/artwork_data.xlsx")

hoja_grafico = cuaderno.add_worksheet('Grafico')

hoja_grafico.write_column('B1', data)
hoja_grafico.write_column('A1', data.index)

chart = cuaderno.add_chart({'type': 'bar'})

chart.add_series({
    'name': 'ARTISTAS',		
    'categories': '=Grafico!$A$1:$A$85',
    'values':     '=Grafico!$B$1:$B$85',
})

hoja_grafico.insert_chart('D2', chart)

cuaderno.close()