
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio con Kmeans
# -- codigo: funciones.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import numpy as np
import pandas as pd
import random
import os
import copy
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
    param_nombre = 'bandera_mexico.jpg'

    """

    # obtener directorio de trabajo actual para encontrar ~/imagenes/archivo.jpg
    directorio = os.getcwd()
    # cargar archivo
    archivo_imagen = im.open(directorio + '/imagenes/' + param_nombre)
    # dejar como array a los datos obtenidos de la imagen
    imagen = np.array(archivo_imagen)
    # asegurarse que el array es escribible
    imagen.setflags(write=True)
    # proceso para hacer reshape y ordenar los datos en N renglones y 3 columnas
    total = archivo_imagen.size[0]*archivo_imagen.size[1]
    # reacomodar para tener todos los datos en una matriz vertical
    datos_imagen = np.reshape(imagen, (total, 3))
    # crear un array de 0s y 4 columnas
    # datos_imagen = np.zeros((total, 4))
    # escribir los datos de los pixeles (3 componentes) y una 4 para apoyo posterior
    # datos_imagen[:, :-1] = imagen

    return {'datos': datos_imagen, 'dimensiones': archivo_imagen.size}


# -- --------------------------------------------------------- FUNCION: Metodo de Kohonen -- #
# -- ------------------------------------------------------------------------------------ -- #
def f_kohonen(param_data, param_k, param_t, param_p):
    """

    Parameters
    ----------
    param_data
    param_k
    param_t
    param_p

    Returns
    -------


    Debugging
    ---------
    param_data = imagen['datos']
    param_k = 2
    param_t = 2
    param_p = 1e-11

    """

    # -------------------------------------------------------------------------------------- #
    # datos de entrada
    datos = param_data.copy()
    datos = datos[:, 0:3]

    # dimensiones
    m = datos.shape[0]
    n = datos.shape[1]

    # objeto vacio para guardar todos los resultados de las iteraciones
    componentes = ['x', 'y', 'z']

    # crear una param_k cantidad de centroides aleatorios
    centroides = (random.randint(np.amin(datos),
                                 np.amax(datos))*np.random.random((3, param_k))).astype(int).T

    # -------------------------------------------------------------------------------------- #

    # error inicial
    error = float("inf")
    # contador de iteraciones inicial
    iteracion = 0

    # -- iteracion para acomodar centroides
    while param_p < error:
        # contador de iteraciones para tamano de paso
        iteracion += 1
        # cuadro de con datos y la clase a la que pertenence
        kohonen_data = pd.concat([pd.DataFrame({'dato_' + componentes[i]: 0 for i in range(n)},
                                               index=np.arange(m)),
                                  pd.DataFrame({'cluster': 0}, index=np.arange(m)),
                                  pd.DataFrame({'cent_' + componentes[i]: 0 for i in range(n)},
                                               index=np.arange(m))], axis=1)

        # -- Distancia un dato a todos los centroides
        for i_dato in range(len(datos)):
            # i_dato = 0
            # objeto con distancias euclidianas
            euclidianas = []
            # -- distancia de cada punto
            for i_centroide in range(param_k):
                # distancia euclidiana del punto con cada centroide
                distancias = np.linalg.norm(datos[i_dato] - centroides[i_centroide])
                # concatenar para cada punto sus distancias con cada centroide
                euclidianas.append(distancias)

            # encontrar el indice de la distancia menor
            cent_dato = np.argmin(euclidianas)

            # centroide encotrado como cercano
            centroides_o = copy.deepcopy(centroides)

            # actualizar tabla de datos + centroides
            kohonen_data.loc[i_dato] = np.append(np.append(datos[i_dato], cent_dato),
                                                 centroides[cent_dato])

            # calcular nueva distancia con tamano de paso para N cantidad de componentes
            comps = [centroides[cent_dato][i] +
                     (datos[i_dato][i] - centroides[cent_dato][i]) * 1 / (param_t + iteracion)
                     for i in range(len(centroides[cent_dato]))]

            # componentes del nuevo centroide
            nvo_centroide = np.vstack(comps)

            # actualizar cada componente del centroide
            for i in range(len(nvo_centroide)):
                centroides[cent_dato][i] = nvo_centroide[i]

            # criterio para decimales, truncarlos a
            centroides = np.trunc(centroides)

            # calcular diferencia de errores
            error = abs(centroides_o - centroides).sum()
            print(error)

        print('centroides originales fueron: ')
        print(centroides)

    # mensaje de salida
    print('el algoritmo convergio en: ' + str(iteracion) + ' iteraciones')

    # kohonen_data

    return 1


# -- --------------------------------------- FUNCION: Calculo de distancia entre vectpres -- #
# -- ------------------------------------------------------------------------------------ -- #

def distancia(param_a, param_b):
    """

    Parameters
    ----------
    param_a : np.array : vector a
    param_b : np.array : vector b

    Returns
    -------
    distancia : int : valor de distancia entre vectores

    Debugging
    ---------
    param_a
    param_b

    """

    # calculo de distancia euclideana
    dist = np.linalg.norm(param_b - param_a)

    return dist


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
    {'datos': k_means_data, 'centroides': centroides}

    Debugging
    ---------
    param_data = imagen['datos']
    param_k = 3
    param_iter = 50

    """

    # datos de entrada
    datos = param_data.copy().astype(int)

    # agregar una 4ta columna para info de centroides
    datos = np.append(datos, np.zeros((datos.shape[0], 1), dtype=int), axis=1)

    # dimensiones
    m = datos.shape[0]
    n = datos.shape[1]

    # objeto vacio para almacenar n cantidad de centroides
    centroides = np.array([]).reshape(n, 0)

    # crear una param_k cantidad de centroides aleatorios
    for _ in range(param_k):
        centroides = np.c_[centroides, datos[random.randint(0, m)]]

    # acomodar con transpuesta
    centroides = centroides.T

    # agregar una 4ta columna para info de centroides
    # datos = np.append(datos, np.zeros((m, 1), dtype=int), axis=1)

    # banderas para while
    iteracion = 0
    error = 2

    while error > 1:
        iteracion += 1
        centroides_n = copy.deepcopy(centroides)
        v = 0

        # distancia de cada dato a los centroides
        for i_dato in datos:
            # i_dato = datos[0]
            distancias = []
            [distancias.append(distancia(param_a=i_dato, param_b=m)) for m in centroides]

            # agregar informacion de centroide correspondiente al dato
            datos[v, n-1] = distancias.index(min(distancias))
            v += 1

        # asignacion de centroides con el promedio de los datos acomodados
        for j in range(param_k):
            for c in range(n):
                centroides[j, c] = np.mean(datos[datos[:, n-1] == j][:, c])

        # calculo de error
        error = np.nanmax(abs(centroides_n - centroides))

        # impresiones de control
        print('\n')
        print('iteracion: ', iteracion)
        print('error: ', error)

    # reasignar valores de centroides a sus respectivos datos
    datos = [centroides[int(i_dato[n-1])] for i_dato in datos]

    return {'datos': datos, 'centroides': centroides}


# -- --------------------------------------------------------- FUNCION: Metodo de K-Means -- #
# -- ------------------------------------------------------------------------------------ -- #

def f_reescribir_imagen(param_data, param_dims, param_nombre):

    """
    Parameters
    ----------
    param_data : np.array : datos de entrada en un array
    param_dims : np.array : con dimensiones de la imagen de salida
    param_nombre : str : nombre del archivo a escribir incluyendo extension

    Returns
    -------

    Debugging
    ---------
    param_dims = imagen['dimensiones']
    param_data = r_kmeans['datos']
    param_nombre = 'kmeans_salida.jpg'

    """

    imagen = np.reshape(np.array(param_data)[:, 0:3], (param_dims[1], param_dims[0], 3))
    datos = imagen.astype(np.uint8)
    nueva_imagen = im.fromarray(datos)

    directorio = os.getcwd()
    nueva_imagen.save(directorio + '/imagenes/' + param_nombre)
