
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
import matplotlib.pyplot as plt

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
param_iter = 5
# cantidad de centroides
param_k = 4
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
componentes = ['x', 'y', 'z']

# ------------------------------------------------------------------------------------------ #

# crear una param_k cantidad de centroides aleatorios
for _ in range(param_k):
    centroides = np.c_[centroides, datos[random.randint(0, m - 1)]]

centroides = centroides.T
centroides_iniciales = centroides.copy()
# objeto con distancias euclidianas

# cuadro de con datos y la clase a la que pertenence
kohonen_data = pd.concat([pd.DataFrame({'dato_' + componentes[i]: 0 for i in range(n)},
                                       index=np.arange(m)),
                          pd.DataFrame({'cluster': 0}, index=np.arange(m)),
                          pd.DataFrame({'cent_' + componentes[i]: 0 for i in range(n)},
                                       index=np.arange(m))], axis=1)

# iteracion para acomodar centroides
for iteracion in range(param_iter):
    # iteracion = 0

    # -- Distancia un dato a todos los centroides
    for i_dato in range(len(datos)):
        # i_dato = 0
        # print('el dato es: ')
        # print(datos[i_dato])
        # print('los centroides son: ')
        # print(centroides)

        # objeto con distancias euclidianas
        euclidianas = []

        for i_centroide in range(param_k):
            # i_centroide = 0
            # distancia euclidiana del punto con cada centroide
            distancias = np.linalg.norm(datos[i_dato] - centroides[i_centroide])
            # concatenar para cada punto sus distancias con cada centroide
            euclidianas.append(distancias)

        # encontrar el indice de la distancia menor
        cent_dato = np.argmin(euclidianas)

        # actualizar tabla de datos + centroides
        kohonen_data.loc[i_dato] = np.append(np.append(datos[i_dato], cent_dato),
                                             centroides[cent_dato])

        # calcular nueva distancia con tamano de paso
        factor = 1/param_p
        nvo_centroide = (centroides[cent_dato] + datos[i_dato])*factor
        # print(nvo_centroide)
        # actualizar cada componente del centroide
        for i in range(len(nvo_centroide)):
            centroides[cent_dato][i] = nvo_centroide[i]

        # print('actualizacion del centroide: ' + str(cent_dato))
        # print(centroides)

# print(centroides_iniciales)
# print(centroides)

colores = ['blue', 'red', 'green', 'brown', 'black']
[plt.scatter(kohonen_data.loc[i][0], kohonen_data.loc[i][1],
             color=colores[int(kohonen_data['cluster'][i])])
 for i in range(len(datos))]
plt.scatter(centroides.T[0], centroides.T[1], s=200, c=colores[0:param_k])
plt.title('Datos a clasificar')
plt.grid()
plt.show()

# ------------------------------------------------------------------------------------------ #
# Dato nuevo para clasificar
dato_nuevo = np.array([[60], [250]])

# calcular distancias
euclidianas = np.array([]).reshape(len(dato_nuevo), 0)

for k in range(param_k):
    distancias = np.sum((dato_nuevo - centroides[k])**2, axis=1)
    # concatenar para cada punto sus distancias con cada centroide
    euclidianas = np.c_[euclidianas, distancias]

cent_ind = np.argmin(euclidianas, axis=1) + 1

# respuesta de texto final
print('el nuevo dato: ' + '[' + str(dato_nuevo[0][0]) + ', ' + str(dato_nuevo[1][0]) + '], ' +
      ' pertenece al centroide: ' + str(cent_ind[0]) + ', el que es de color: ' +
      colores[cent_ind[0] - 1])

# ------------------------------------------------------------------------------------------ #

# codigo para visualizacion
colores = ['blue', 'red', 'green', 'brown', 'black']
[plt.scatter(kohonen_data.loc[i][0], kohonen_data.loc[i][1],
             color=colores[int(kohonen_data['cluster'][i])])
 for i in range(len(datos))]
plt.scatter(centroides.T[0], centroides.T[1], s=200, c='grey')
plt.scatter(centroides.T[0], centroides.T[1], s=100, c='white')

plt.scatter(dato_nuevo[0, :], dato_nuevo[1, :], s=150, c=colores[cent_ind[0] - 1])
plt.scatter(dato_nuevo[0, :], dato_nuevo[1, :], s=100, c='white')
plt.scatter(dato_nuevo[0, :], dato_nuevo[1, :], s=25, c=colores[cent_ind[0] - 1])

plt.title('Datos a clasificar')
plt.grid()
plt.show()
