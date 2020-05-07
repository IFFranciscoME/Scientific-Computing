
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio con Simulated Annealing - Parte 1
# -- codigo: IDI_II_Tarea_5_SA_P1_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

"""
1.- Con la tabla de distancias 8c_test, encuentre el ciclo de valor mínimo usando el algoritmo
“Simulated Annealing (SA)”. Decida la manera de decrementar la temperatura para obtener la
mejor respuesta que le sea posible. Repita el algoritmo varias veces y encuentre el menor
valor de todas las corridas, escriba la desviación estándar de las respuestas obtenidas. No
verifique más del 1% de las permutaciones. Escriba las configuraciones utilizadas y el número
de rutas que fueron revisadas.

2.- Ahora encuentre el ciclo de valor mínimo para la tabla 20c_test. No hay límite de
configuraciones. De nuevo escriba las configuraciones utilizadas y el número de rutas revisado
"""

import pandas as pd
import numpy as np
import random
import math
import statistics

# random.seed(2020)
# leer datos de entrada
data = pd.read_excel('archivos/dist.xlsx', sheet_name='8c_test')
# asignar a index los nombres de las ciudades
data.index = data.iloc[:, 0]
ciudades = data.iloc[:, 0]
# quitar primera columna de nombres
data = data.iloc[:, 1:]
# hacer un array con solo el contenido del dataframe
np_data = np.array(np.nan_to_num(data))

# -------------------------------------------------------- Algoritmo: Simulated Annealing -- #

# para guardar las distancias minimas que se fueron encontrando
distancias_varias = []
# para guardar todas las rutas que se visitaron
rutas_varias = []
# cantidad de corridas del algoritmo
n_corridas = 100
# contador
contador = 0

# -- Parametros SA
# datos vecinos revisados aleatoriamente
N = 3
# factor de disminucion para T
factor_t = 0.99
# --

# para controlar permutaciones maximas
permutaciones = math.factorial(len(np_data[1, :]))/2
perm_max = int(permutaciones*0.01)

# -- ----------------------------------------------------------------------------- SA -- #
for j in range(0, n_corridas):

    # configuracion inicial aleatoria
    recorrido_rand = list(np.arange(len(np_data[:, 0])))
    random.shuffle(recorrido_rand)
    C1 = recorrido_rand

    # objetos para guardar rutas y distancias
    rutas = []
    distancias = []

    # valor inicial de Temperatura
    T = 100

    # (10) mientras T sea  1 se repetira el proceso
    while T > 1:
        contador += 1
        # (p8) cantidad de configuraciones de parametros "cercanas" en los que se busca
        for n_iter in range(0, N):
            # N = 2
            # (p3) Intercambiar 2 posiciones en la lista de 1 config de parametros
            C2 = list(C1)
            inter = list(np.random.choice(C1, 2, replace=False))
            C2[inter[0]], C2[inter[1]] = C2[inter[1]], C2[inter[0]]

            # (p4) Calcular distancia entre la anterior y la nueva config de parametros
            E1 = sum([np_data[C1[j]][C1[j+1]] for j in range(0, len(C1)-1)])
            E2 = sum([np_data[C2[k]][C2[k+1]] for k in range(0, len(C2)-1)])

            # (p5) calcular decremento de medida de error
            q = math.e**((E1-E2)/T)

            # (p6 y p7) aceptar o rechazar aleatoriamente la config de parametros nueva
            p = np.random.random(1)[0]
            if p < q:
                C1 = C2

            # p(11) guardar en lista el valor de la configuracion actual
            rutas.append(C1)
            # lista de distancias totales por ruta
            distancias.append(sum([np_data[C1[i]][C1[i+1]] for i in range(0, len(C1)-1)]))

        # 9.- Disminuya en 10% el valor de T
        T = T*factor_t

    print('\n corrida numero = ', j)
    id_distancia_minima = np.argmin(distancias)
    distancia_minima = np.argmin(distancias)
    print('permutaciones maximas: ', perm_max)
    print('permutaciones hechas: ', len(distancias))
    print('distancia minima encontrada: ', distancias[distancia_minima])
    ruta_distancia_minima = rutas[distancia_minima]
    ciudades = list(ciudades)
    recorrido = [ciudades[ruta_distancia_minima[c]] for c in range(0, len(ciudades))]
    print('el recorrido fue: ', recorrido)

    distancias_varias.append(distancias[distancia_minima])
    rutas_varias.append(recorrido)

desv_est = statistics.stdev(distancias_varias)
print('\n \n--- ')
print('rutas revisadas: ', contador)
print('la ruta con distancia minima: ',
      rutas_varias[np.argmin(distancias_varias)])
print('distancia de la ruta: ',
      distancias_varias[np.argmin(distancias_varias)])
print('desviacion estandar de distancias minimas: ', desv_est)

# 1)
# T=1000, N=3, factor_t=0.80 ; rutas = 3100, minimo de 6029 ; con desvest = 849.33
# T=500, N=3, factor_t=0.90 ; rutas = 5900, minimo de 6029 ; con desvest = 705.16
# T=100, N=3, factor_t=0.99 ; rutas = 45900, minimo de 6029 ; con desvest = 678.28

# 2)
# T=500, N=10, factor_t=0.80 ; rutas = 2800, minimo de 1232.25 ; con desvest = 131.84
# T=500, N=20, factor_t=0.90 ; rutas = 5900, minimo de 1044.89 ; con desvest = 88.77
# T=500, N=25, factor_t=0.95 ; rutas = 12200, minimo de 1038.44 ; con desvest = 83.67
# T=500, N=30, factor_t=0.99 ; rutas = 61900, minimo de 996.12 ; con desvest = 67.80

# ruta con distancia minima encontrada para 2)
# ['Alista', 'Atacco', 'Atemajac de Brizuela', 'Amacueca', 'Acatlán de Juárez',
# 'Atengo', 'Atenguillo', 'Ameca', 'Ahualulco de Mercado', 'Antonio Escobedo',
# 'Amatitán', 'Ahuisculco', 'Altus Bosques', 'Acatic', 'Ajijic', 'Atequiza',
# 'Ahuatlán', 'Atotonilco el Alto', 'Arandas', 'Allende']
