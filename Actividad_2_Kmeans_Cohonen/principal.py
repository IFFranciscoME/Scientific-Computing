
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

# busca en el sistema el directorio donde este la carpeta
abspath = path.abspath('imagenes/')

# extrae todos los nombres de los archivos dentro de esa carpeta
archivos = [f for f in listdir(abspath) if isfile(join(abspath, f))]
# ['bandera_alemania.jpg', 'bandera_mexico.jpg', 'paisaje_riscos.jpg', 'persona_gandhi.jpg']

# obtener los datos de la imagen
imagen = fn.f_entrada_imagenes(param_nombre=archivos[0])

# obtener resultados con k-means
# r_kmeans = fn.f_kmeans(param_data=imagen['datos'], param_k=3, param_iter=50)

# reescribir la imagen
# fn.f_reescribir_imagen(param_data=imagen['datos'], param_dims=imagen['dimensiones'],
#                        param_nombre='kmeans_salida.jpg')

# obtener resultados con Kohonen
# resultados_kmean = fn.f_kmeans(param_data=datos_imagen, param_k=3, param_iter=10)

# reescribir la imagen
# fn.f_reescribir_imagen(param_data=imagen['datos'])
