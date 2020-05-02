
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

import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

# -- ------------------------------------------------------------------------ Datos extra -- #
directorio = os.getcwd()
datos = pd.read_csv(directorio + '/Tarea_9_Kmeans/archivos/' + 'datos.csv')

# normalizar datos
datos['x'] = datos['x']/max(datos['x'])
datos['y'] = datos['y']/max(datos['y'])

# -- ---------------------------------------------------------------------- Visualizacion -- #
fig, ax = plt.subplots()
x, y = datos['x'], datos['y']
ax.scatter(x, y)
ax.grid(True)
plt.show()

# -- ---------------------------------------------------------------------------- K-means -- #

# cantidad de K
modelo_k = 2

# semilla para debugging
np.random.seed(2020)

# array de n-dimensiones

# rango de variables
rango_x = np.arange(min(x), max(x))
rango_y = np.arange(min(y), max(y))

# -- PASO 1: inicializacion de centroides

# -- PASO 2: Calcular distancia de cada punto a los centroides

# -- PASO 3: Cada dato asignarle la clase del centroide al que este mas cerca

# -- PASO 4: Calcular promedio de las distancias de cada dato a su centroide

# -- PASO 5: Obtener las coordenadas del nuevo centroide

# -- PASO 6: Verificar si alcanza el criterio de paro

# criterio de paro es que las clases no cambian

# -- PASO 7: Finalizar si hay criterio de paro o repetir si no lo hubo

