
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio con Kmeans
# -- codigo: IDI_II_Tarea_9_Kmeans_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

"""
Realizar código en Python que reciba una tabla de datos numéricos organizados en 2 columnas
(x,y) y devuelva los centroides de k>=2 clases usando k-medias. Inicialice los centroides con
valores aleatorios (de forma uniforme en el rango de valores de cada columna).

Luego, realice código que reciba una pareja de valores (x,y) y devuelva a qué clase pertenece
de acuerdo a la clasificación obtenida anteriormente.
"""

import numpy as np
import os
import pandas as pd

# ------------------------------------------------------------------------------------------ #
directorio = os.getcwd()
df_datos = pd.read_csv(directorio + '/Tarea_9_Kmeans/archivos/' + 'datos.csv')

# normalizar datos
df_datos['x'] = df_datos['x']/max(df_datos['x'])
df_datos['y'] = df_datos['y']/max(df_datos['y'])
datos = np.array([list(df_datos['x']), list(df_datos['y'])]).T
# ------------------------------------------------------------------------------------------ #
