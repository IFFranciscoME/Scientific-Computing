
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Actividad 2: Kohonen y K-medias
# -- codigo: principal.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import funciones as fn
import numpy as np

# Semilla para aleatorios
np.random.seed(2020)
# Las iteraciones son el criterio de paro
param_iter = 50
# cantidad de centroides
param_k = 3

# obtener los datos de la imagen
datos_imagen = fn.f_entrada_imagenes(param_nombre='persona_gandhi.jpg')

# obtener resultados con k-means
resultados_kmean = fn.f_kmeans(param_data=datos_imagen, param_k=3, param_iter=10)

# obtener resultados con Kohonen
# resultados_kmean = fn.f_kmeans(param_data=datos_imagen, param_k=3, param_iter=10)
