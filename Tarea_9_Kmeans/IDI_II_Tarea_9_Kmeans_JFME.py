
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
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------------ #

# para correr en mi compu uso estas lineas
directorio = os.getcwd()
df_datos = pd.read_csv(directorio + '/Tarea_9_Kmeans/archivos/' + 'datos.csv')

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
k_means_data = dict()
# ------------------------------------------------------------------------------------------ #

# crear una param_k cantidad de centroides aleatorios
for _ in range(param_k):
    centroides = np.c_[centroides, datos[random.randint(0, m - 1)]]

# ------------------------------------------------------------------------------------------ #

# iteraciones de busqueda y ajuste
for i in range(param_iter):

    # objeto con distancias euclidianas
    euclidianas = np.array([]).reshape(m, 0)

    # para cada centroide calcular las distancias a cada punto
    for k in range(param_k):
        # distancia euclidiana de cada punto con cada centroide
        distancias = np.sum((datos-centroides[:, k])**2, axis=1)
        # concatenar para cada punto sus distancias con cada centroide
        euclidianas = np.c_[euclidianas, distancias]

    # encontrar indice de columna con la distancia minima de cada punto a cada centroide
    cent_ind = np.argmin(euclidianas, axis=1) + 1
    cent_data = {}

    # una lista de arrays, uno para cada centroide
    for lista in range(param_k):
        cent_data[lista + 1] = np.array([]).reshape(n, 0)

    # asociar datos a su centroide y concatenar todos los centroides
    for con in range(m):
        cent_data[cent_ind[con]] = np.c_[cent_data[cent_ind[con]], datos[con]]

    # reacomodo de datos y parametro de k-mean
    for dato in range(param_k):
        # dar formato a arrays de datos en centroides
        cent_data[dato + 1] = cent_data[dato + 1].T
        # calcular el promedio de distancias de datos al centroide para cada centroide
        centroides[:, dato] = np.mean(cent_data[dato + 1], axis=0)

    # Dejar resultados finales en un diccionario
    k_means_data.update(cent_data)
# ------------------------------------------------------------------------------------------ #

# codigo para visualizacion
colores = ['blue', 'red', 'green', 'brown', 'black']
[plt.scatter(k_means_data[i + 1][:, 0], k_means_data[i + 1][:, 1], color=colores[i])
 for i in range(param_k)]
plt.scatter(centroides[0, :], centroides[1, :], s=200, c='grey')
plt.scatter(centroides[0, :], centroides[1, :], s=100, c='white')
plt.title('Datos a clasificar')
plt.show()

# ------------------------------------------------------------------------------------------ #
# Dato nuevo para clasificar
dato_nuevo = np.array([[60], [250]])

# calcular distancias
euclidianas = np.array([]).reshape(len(dato_nuevo), 0)

for k in range(param_k):
    distancias = np.sum((dato_nuevo - centroides[:, k])**2, axis=1)
    # concatenar para cada punto sus distancias con cada centroide
    euclidianas = np.c_[euclidianas, distancias]

cent_ind = np.argmin(euclidianas, axis=1) + 1

# respuesta de texto final
print('el nuevo dato: ' + '[' + str(dato_nuevo[0][0]) + ', ' + str(dato_nuevo[1][0]) + '], ' +
      ' pertenece al centroide: ' + str(cent_ind[0]) + ', el que es de color: ' +
      colores[cent_ind[0] - 1])
