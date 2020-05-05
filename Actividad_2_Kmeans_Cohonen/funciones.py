
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
    imagen = np.reshape(imagen, (total, 3))
    # crear un array de 0s y 4 columnas
    datos_imagen = np.zeros((total, 4))
    # escribir los datos de los pixeles (3 componentes) y una 4 para apoyo posterior
    datos_imagen[:, :-1] = imagen

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

            # criterio para decimales, truncarlos a 0
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

    # copiar datos originales en objeto nuevo quintando la 4ta columna
    data = param_data.copy()[:, :-1]

    # dimensiones
    m = data.shape[0]
    n = data.shape[1]

    # objeto vacio para almacenar n cantidad de centroides
    centroides = np.array([]).reshape(n, 0)

    # objeto vacio para guardar todos los resultados de las iteraciones
    k_means_data = dict()

    # -------------------------------------------------------------------------------------- #

    # crear una param_k cantidad de centroides aleatorios
    for _ in range(param_k):
        centroides = np.c_[centroides, data[random.randint(0, m - 1)]]
    print(centroides)

    # -------------------------------------------------------------------------------------- #

    # iteraciones de busqueda y ajuste
    # iteraciones de busqueda y ajuste
    for i in range(param_iter):

        # objeto con distancias euclidianas
        euclidianas = np.array([]).reshape(m, 0)

        # para cada centroide calcular las distancias a cada punto
        for k in range(param_k):
            # distancia euclidiana de cada punto con cada centroide
            distancias = np.sum((data - centroides[:, k]) ** 2, axis=1)
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
            cent_data[cent_ind[con]] = np.c_[cent_data[cent_ind[con]], data[con]]

        # reacomodo de datos y parametro de k-mean
        for dato in range(param_k):
            # dar formato a arrays de datos en centroides
            cent_data[dato + 1] = cent_data[dato + 1].T
            # calcular el promedio de distancias de datos al centroide para cada centroide
            centroides[:, dato] = np.mean(cent_data[dato + 1], axis=0)

        # reacomodo de valores para centroides
        centroides = centroides.T

        # para llaves iguales, les actualiza los valores
        k_means_data.update(cent_data)

    # dataframe final
    df_final = pd.concat([pd.concat([pd.DataFrame(k_means_data[i]),
                                     pd.DataFrame({'centroide': [i]*len(k_means_data[i])})],
                                    axis=1) for i in range(1, len(centroides)+1)])

    cents = list(k_means_data.keys())

    for i in cents:
        df_final.iloc[np.where(df_final['centroide'] == i)[0], 0:3] = list(centroides[i-1])
    df_final.reset_index(drop=True, inplace=True)

    return {'datos': df_final, 'centroides': centroides}


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
