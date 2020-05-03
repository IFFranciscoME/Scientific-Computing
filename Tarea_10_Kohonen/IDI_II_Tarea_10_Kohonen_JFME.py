
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
import random
import os
import pandas as pd

# ------------------------------------------------------------------------------------------ #

# para correr en mi compu uso estas lineas
directorio = os.getcwd()
df_datos = pd.read_csv(directorio + '/archivos/' + 'datos.csv')

# para revision utilizar esta linea
# df_datos = pd.read_csv('datos.csv')
# ------------------------------------------------------------------------------------------ #

# Las iteraciones son el criterio de paro
param_iter = 100
# cantidad de centroides
param_k = 3

# ------------------------------------------------------------------------------------------ #
# objeto para guardar datos de entrada
datos = np.array([list(df_datos['x']), list(df_datos['y'])]).T
# dimensiones
m = datos.shape[0]
n = datos.shape[1]
# objeto vacio para almacenar n cantidad de centroides
centroides = np.array([]).reshape(n, 0)
# objeto vacio para guardar todos los resultados de las iteraciones
kohonen_data = dict()
# ------------------------------------------------------------------------------------------ #

# crear una param_k cantidad de centroides aleatorios
for _ in range(param_k):
    centroides = np.c_[centroides, datos[random.randint(0, m - 1)]]
