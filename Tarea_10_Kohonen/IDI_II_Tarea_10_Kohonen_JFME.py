
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio con Kmeans
# -- codigo: IDI_II_Tarea_10_Kohonen_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

"""
Realizar código en Python que reciba una tabla de datos numéricos organizados en
2 columnas (x,y) y devuelva los centroides de k>=2 clases usando una red de Kohonen.
Inicialice los centroides con valores aleatorios (de forma uniforme en el rango de valores
de cada columna). Utilice tamaños de paso a partir de 2 que aumenten linealmente, y detenga
el proceso cuando no haya centroide que presente un cambio significativo
(a su nivel de precisión).

Luego, realice código que reciba una pareja de valores (x,y) y devuelva a qué clase pertenece
de acuerdo a la clasificación obtenida anteriormente.
"""

import numpy as np
import pandas as pd
import os
import random

# ------------------------------------------------------------------------------------------ #

# para correr en mi compu uso estas lineas
directorio = os.getcwd()
df_datos = pd.read_csv(directorio + '/archivos/' + 'datos.csv')

# para revision utilizar esta linea
# df_datos = pd.read_csv('datos.csv')
# ------------------------------------------------------------------------------------------ #

# Semilla para aleatorios
np.random.seed(2020)
# Las iteraciones son el criterio de paro
param_iter = 100
# cantidad de centroides
param_k = 3
# tamano de paso
param_p = 2

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

# objeto con distancias euclidianas


# -- Distancia un dato a todos los centroides

for i_dato in range(len(datos)):
    i_dato = 2
    print(datos[i_dato])
    print(centroides)

    # objeto con distancias euclidianas
    euclidianas = []

    for i_centroide in range(param_k):
        # distancia euclidiana del punto con cada centroide
        distancias = np.sum((datos[i_dato] - centroides[:, i_centroide])**2, axis=0)
        # concatenar para cada punto sus distancias con cada centroide
        euclidianas.append(distancias)

    # segun la menor distancia es el centroide que le corresponde
    cent_dato = np.argmin(euclidianas)
    # calcular nueva distancia con tamano de paso
    # distancia entre posicion actual del centroide y del dato

    centroides.T[0] - (datos[i_dato])

    # centroides[0][cent_dato] = centroides[0][cent_dato] * 1/param_p
    # centroides[1][cent_dato] = centroides[1][cent_dato] * 1/param_p

# concatenar para cada punto sus distancias con cada centroide
euclidianas = np.c_[euclidianas, distancias]
