
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio con Kmeans
# -- codigo: funciones.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import numpy as np
import random
import os
from PIL import Image as im


# -- ------------------------------------------------------- FUNCION: Lectura de imagenes -- #
# -- ------------------------------------------------------------------------------------ -- #
def f_entrada_imagenes(param_nombre):
    """

    Parameters
    ----------
    param_nombre : str : Nombre del archivo a leer

    Returns
    -------

    Debugging
    ---------
    param_nombre = 'persona_gandhi.jpg'

    """
    directorio = os.getcwd()
    imagen = im.open(directorio + '/imagenes/' + param_nombre)
    a = np.array(imagen)
    a.setflags(write=1)
    total = imagen.size[0]*imagen.size[1]
    a = np.reshape(a, (total, 3))
    tabla = np.zeros((total, 4))
    tabla[:, :-1] = a

    return tabla


# -- --------------------------------------------------------- FUNCION: Metodo de K-Means -- #
# -- ------------------------------------------------------------------------------------ -- #
def f_kmeans(param_data, param_k, param_iter):
    """

    Parameters
    ----------
    param_data : np.array : array con N cantidad de columnas para N dimensiones
    param_k : int : cantidad de clusters a utilizar para la clasificacion
    param_iter : int : cantidad de iteraciones

    Returns
    -------

    Debugging
    ---------
    param_data = datos_imagen
    param_k = 3
    param_iter = 50

    """

    # dimensiones
    m = param_data.shape[0]
    n = param_data.shape[1]
    # objeto vacio para almacenar n cantidad de centroides
    centroides = np.array([]).reshape(n, 0)
    # objeto vacio para guardar todos los resultados de las iteraciones
    k_means_data = dict()
    # -------------------------------------------------------------------------------------- #

    # crear una param_k cantidad de centroides aleatorios
    for _ in range(param_k):
        centroides = np.c_[centroides, param_data[random.randint(0, m - 1)]]

    # -------------------------------------------------------------------------------------- #

    # iteraciones de busqueda y ajuste
    for i in range(param_iter):

        # objeto con distancias euclidianas
        euclidianas = np.array([]).reshape(m, 0)

        # para cada centroide calcular las distancias a cada punto
        for k in range(param_k):
            # distancia euclidiana de cada punto con cada centroide
            distancias = np.sum((param_data - centroides[:, k]) ** 2, axis=1)
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
            cent_data[cent_ind[con]] = np.c_[cent_data[cent_ind[con]], param_data[con]]

        # reacomodo de datos y parametro de k-mean
        for dato in range(param_k):
            # dar formato a arrays de datos en centroides
            cent_data[dato + 1] = cent_data[dato + 1].T
            # calcular el promedio de distancias de datos al centroide para cada centroide
            centroides[:, dato] = np.mean(cent_data[dato + 1], axis=0)

        # Dejar resultados finales en un diccionario
        k_means_data.update(cent_data)

    return k_means_data
