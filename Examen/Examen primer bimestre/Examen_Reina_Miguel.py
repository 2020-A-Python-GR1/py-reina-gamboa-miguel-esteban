# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:00:05 2020

@author: migue
"""

import numpy as np
import pandas as pd
import os
from scipy import ndimage
from scipy import misc

vector_diez_cero = np.zeros(10)
print("2.-")
print(vector_diez_cero)
vector_diez_cero[5] = 1
print("3.-")
print(vector_diez_cero)
vector_cincuenta_elementos = np.arange(50)
print(vector_cincuenta_elementos)
print("4.-")
print(vector_cincuenta_elementos[::-1])
arreglo_tres_por_tres = np.arange(9)
matriz_tres_por_tres = arreglo_tres_por_tres.reshape(3, 3)
print("5.-")
print(matriz_tres_por_tres)
arreglo = [1,2,0,0,4,0]
muestra_uno = np.array(arreglo)
mayores_cero = muestra_uno > 0
print("6.-")
print(muestra_uno[mayores_cero])
matriz_identidad = np.eye(3)
print("7.-")
print(matriz_identidad)
matriz_random = np.random.rand(3, 3, 3)
print("8.-")
print(matriz_random)
matriz_diez_por_diez = np.random.randint(0, 1000, 100)
matriz_busqueda = matriz_diez_por_diez.reshape(10, 10)
print(matriz_busqueda)
print("9.-")
print(matriz_busqueda.min())
print(matriz_busqueda.max())
imag = misc.face()
rgb = imag.reshape(imag.shape[0]*imag.shape[1], imag.shape[2])
rgb_uno = np.unique(rgb, axis=0)
print("10.-")
print(rgb_uno)
print(rgb_uno[-1])
print("Series.")
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
serie_a = pd.Series(mylist)
serie_b = pd.Series(myarr)
serie_c = pd.Series(mydict)
print("11.-")
print(serie_a)
print(serie_b)
print(serie_c)
df_exam = pd.DataFrame(serie_c)
print("12.-")
print(df_exam)
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
df_0 = pd.DataFrame(ser1)
df_0[1] = ser2
print("13.-")
print(df_0)
df_1 = pd.DataFrame(ser1, ser2)
print(df_1)
ser01 = pd.Series([1, 2, 3, 4, 5])
ser02 = pd.Series([4, 5, 6, 7, 8])
series_add = ser01[~ser01.isin(ser02)]
print("14.-")
print(series_add)
series_add_uno = ser01[~ser01.isin(ser02)]
series_add_dos = ser02[~ser02.isin(ser01)]
series_result = series_add_uno.append(series_add_dos)
print("15.-")
print(series_result)
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
print("16.-")
print(ser.value_counts())
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
result = ser[pos]
print("19.-")
print(result)
print("22.-")
path = "C:/Users/migue/OneDrive/Documentos/EPN/Sexto Semestre/Desarrollo web con python/Github/py-reina-gamboa-miguel-esteban/Examen/Examen primer bimestre/BostonHousing.csv"
columns = ["crim", "zn", "indus", "chas"]
df_read =pd.read_csv(path, nrows = 4, usecols = columns)
