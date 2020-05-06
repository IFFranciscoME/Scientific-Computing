
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Actividad 2: Kohonen y K-medias
# -- codigo: principal.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import funciones as fn
import numpy as np
from os import listdir, path
from os.path import isfile, join

# Semilla para aleatorios
np.random.seed(2020)

# -------------------------------------------------------------- generar datos de entrada -- #
# busca en el sistema el directorio donde este la carpeta
abspath = path.abspath('imagenes/originales/')

# extrae todos los nombres de los archivos dentro de esa carpeta
archivos = [f for f in listdir(abspath) if isfile(join(abspath, f))]

# numero de archivo
# 0 -> 'bandera_alemania.jpg', 1 -> 'bandera_mexico.jpg',
# 2 -> 'paisaje_riscos.jpg', 3 -> 'persona_gandhi.jpg'
archivo = 3
# obtener los datos de la imagen
imagen = fn.f_entrada_imagenes(param_nombre=archivos[archivo])
# K para correr pruebas
k = 2

# -- ---------------------------------------------------------------------------- K-MEANS -- #
# obtener resultados con k-means
r_kmeans = fn.f_kmeans(param_data=imagen['datos'], param_k=k, param_t=50, param_p=1e-1)

# reescribir la imagen
fn.f_reescribir_imagen(param_data=r_kmeans['datos'], param_dims=imagen['dimensiones'],
                       param_nombre='/kmeans/' + archivos[archivo][0:-4] +
                                    '_kmeans_i50_k' + str(k) + '.jpg')

# Para K=20 en la imagen persona_gandhi.jpg
# iteracion:  38
# error:  0.07877499425418932
# tiempo: 39 segundos aprox

# -- ---------------------------------------------------------------------------- KOHONEN -- #
# obtener resultados con Kohonen
r_kohonen = fn.f_kohonen(param_data=imagen['datos'], param_k=k, param_t=50, param_p=1e-1)

# reescribir la imagen
fn.f_reescribir_imagen(param_data=r_kohonen['datos'], param_dims=imagen['dimensiones'],
                       param_nombre='/kohonen/' + archivos[archivo][0:-4] +
                                    '_kohonen_i50_k' + str(k) + '.jpg')

# Para K=20 en la imagen persona_gandhi.jpg
# iteracion:  274
# error:  0.09993658905139569
# tiempo: 12 minutos aprox
