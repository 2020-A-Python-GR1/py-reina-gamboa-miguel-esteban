import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

path = "C:/Users/migue/OneDrive/Escritorio/git/py-reina-gamboa-miguel-esteban/Deberes/Deber_06/top50.csv"
columnas = ['Track.Name','Artist.Name','Genre','Beats.Per.Minute','Energy','Danceability','Loudness..dB..','Liveness','Valence.','Length.','Acousticness..','Speechiness.','Popularity']

df1 = pd.read_csv(path, 
                  usecols=columnas)