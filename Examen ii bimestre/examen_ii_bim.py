import numpy as np
import pandas as pd
import os
from datetime import date

print("Examen ii bimestre")
print("Miguel Esteban Reina Gamboa")

print("1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros")
arr_pand = np.random.randint(1, 10, 60).reshape(10, 6)
df1 = pd.DataFrame(arr_pand)
s1 = df1[:5]
s2 = df1[5:]
print(df1)
print("------------")
print(s1)
print("------------")
print(s2)

print("2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico")
arreglo = np.random.randint(1, 10, 24).reshape(6, 4)
columnas = ['A', 'B', 'C', 'D']
indices = [date.today(),
           date.today(),
           date.today(),
           date.today(),
           date.today(),
           date.today()
        ]
df2 = pd.DataFrame(
        arreglo,
        columns = columnas,
        index = indices
        )
print("Indices\n",indices)
print("Dataframe\n",df2)

print("4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.")
arr4 = np.random.randint(1, 10, 60).reshape(10, 6)
df4 = pd.DataFrame(arr4)
col_df4 = df4.columns.values
val = df4.values
print(col_df4)
print("------------")
print(val)

print("5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe")
arr5 = np.random.randint(1, 10, 60).reshape(10, 6)
df5 = pd.DataFrame(arr5)
df_d = df5.describe()
print(df_d)

print("6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos")
arr6 = np.random.randint(1, 10, 60).reshape(10, 6)
df6 = pd.DataFrame(arr6)
df_t = df6.transpose()
print(df_t)

print("7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente")
arr7 = np.random.randint(1, 10, 60).reshape(10, 6)
df7 = pd.DataFrame(arr7)
df7_ascendente = df7.apply(lambda x: x.sort_values().values)
df7_descendente = df7.apply(lambda x: x.sort_values(ascending = False).values)
print(df7_ascendente)
print("------------")
print(df7_descendente)

print("8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7")
arr8 = np.random.randint(1, 10, 60).reshape(10, 6)
df8 = pd.DataFrame(arr8)
may_a_7 = df8 > 7
df_may_7 = df8[may_a_7]
print(df_may_7)

print("9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.")
arr9 = np.random.randint(1, 10, 60).reshape(10, 6)
df9 = pd.DataFrame(arr9)
may_a_5 = df9 > 5
df_may_5 = df9[may_a_5]
df_ceros = df_may_5.fillna(0)
print(df_ceros)

print("10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio")
arr10 = np.random.randint(1, 10, 60).reshape(10, 6)
df10 = pd.DataFrame(arr10)
media = df10.mean()
mediana = df10.median()
promedio = df10.mean()
print(df10)
print("------------")
print(media)
print("------------")
print(mediana)
print("------------")
print(promedio)

print("11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe")
arr11_1 = np.random.randint(1, 10, 60).reshape(10, 6)
df11_1 = pd.DataFrame(arr11_1)
arr11_2 = np.random.randint(1, 10, 60).reshape(10, 6)
df11_2 = pd.DataFrame(arr11_2)
df11_final = df11_1.append(df11_2)
print(df11_final)

print("12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.")
arr12 = pd.util.testing.rands_array(3, 60).reshape(10,6)
df12 = pd.DataFrame(arr12)
df12_final = pd.DataFrame(df12[0] + df12[1])
df12_final[1] = df12[2] + df12[3]
df12_final[2] = df12[4] + df12[5]
print(df12_final[1])
print("------------")
print(df12_final[2])

print("13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna")
arr13 = np.random.randint(1, 10, 60).reshape(10, 6)
df13 = pd.DataFrame(arr13)
for column in df13.columns:
    print("Columna " + str(column))
    print(df13[column].value_counts())

print("14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. Crear una nueva columna con el calculo por fila (A * B ) / C")
arr14 = np.random.randint(1, 10, 30).reshape(10, 3)
df14 = pd.DataFrame(arr14, columns = ['A', 'B', 'C'])
print(df14)
print("------------")
print(df14['A'][0])
resultados = []
for index in df14.index:
    resultados.append((df14['A'][index] * df14['B'][index]) / df14['C'][index] )    
print(resultados)
df14['Resultados'] = resultados