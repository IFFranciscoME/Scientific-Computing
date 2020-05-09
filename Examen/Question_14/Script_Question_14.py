
#

import pandas as pd
import numpy as np
import random
import math
import statistics

# random.seed(2020)
# leer datos de entrada
data = pd.read_excel('Question_14/archivos/dist.xlsx', sheet_name='Question_14')
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
n_corridas = 2


# -- Parametros SA
# datos vecinos revisados aleatoriamente
N = 3
# T
T = 100
# factor de disminucion para T
factor_t = 0.5
# --

# para controlar permutaciones maximas
permutaciones = math.factorial(len(np_data[1, :]))/2
perm_max = int(permutaciones*1/1000)

# -- ----------------------------------------------------------------------------- SA -- #
for j in range(0, n_corridas):
    # j = 0

    # contador para permutaciones maximas
    contador = 0

    # configuracion inicial aleatoria
    recorrido_rand = list(np.arange(len(np_data[:, 0])))
    random.shuffle(recorrido_rand)
    C1 = recorrido_rand

    # hacer ciclica o no ciclica la ruta
    # agregar primer numero al ultimo para C1 y para C2
    C1.append(C1[0])

    # objetos para guardar rutas y distancias
    rutas = []
    distancias = []

    # valor inicial de Temperatura
    T_iter = T
    itera_t = 0

    # (10) mientras T sea  1 se repetira el proceso
    while T_iter > 1:
        itera_t += 1
        # (p8) cantidad de configuraciones de parametros "cercanas" en los que se busca
        for n_iter in range(0, N):
            # n_iter = 0

            # (p3) Intercambiar 2 posiciones en la lista de 1 config de parametros
            C2 = list(C1)
            ind_C1 = np.arange(1, len(C1)-1)
            inter = list(np.random.choice(ind_C1, 2, replace=False))
            # modificacion para que no haga shuffle del 1er y ultimo valor (inicio-fin)
            # de la ruta.
            C2[inter[0]], C2[inter[1]] = C2[inter[1]], C2[inter[0]]

            # (p4) Calcular distancia entre la anterior y la nueva config de parametros
            E1 = sum([np_data[C1[j]][C1[j+1]] for j in range(0, len(C1)-1)])
            E2 = sum([np_data[C2[k]][C2[k+1]] for k in range(0, len(C2)-1)])

            # contador de permutaciones verificadas
            contador += 2

            # (p5) calcular decremento de medida de error
            q = math.e ** ((E1 - E2) / T)

            # (p6 y p7) aceptar o rechazar aleatoriamente la config de parametros nueva
            p = np.random.random(1)[0]
            if p < q:
                C1 = C2

            # p(11) guardar en lista el valor de la configuracion actual
            rutas.append(C1)
            # lista de distancias totales por ruta
            distancias.append(sum([np_data[C1[i]][C1[i+1]] for i in range(0, len(C1)-1)]))

        # 9.- Disminuya en 10% el valor de T

        print(itera_t)
        # (1)
        # T_iter = T_iter*factor_t

        # (2)
        # T_iter = T_iter/np.log(n_iter)

        # (3)
        T_iter = math.exp(-itera_t)*T_iter
        print(T_iter)

    print('\n corrida numero = ', j)
    id_distancia_minima = np.argmin(distancias)
    distancia_minima = np.argmin(distancias)
    print('permutaciones maximas: ', perm_max)
    print('permutaciones hechas: ', contador)
    print('distancia minima encontrada: ', distancias[distancia_minima])
    ruta_distancia_minima = rutas[distancia_minima]
    ciudades = list(ciudades)
    recorrido = [ciudades[ruta_distancia_minima[c]] for c in range(0, len(ciudades)+1)]
    print('el recorrido fue: ', recorrido)

    distancias_varias.append(distancias[distancia_minima])
    rutas_varias.append(recorrido)

desv_est = statistics.stdev(distancias_varias)
print('\n \n----------------------------------- ')
print('Configuracion: ' 'T =', T, ' | N =', N, ' | factor_t =', factor_t)
print('permutaciones maximas: ', perm_max)
print('rutas revisadas por iteracion: ', contador)
print('rutas totales revisadas en ', j+1, ' iteraciones: ', contador*j)
print('la ruta con distancia minima: ', rutas_varias[np.argmin(distancias_varias)])
print('distancia de la ruta mínima: ', distancias_varias[np.argmin(distancias_varias)])
print('desviacion estandar de distancias minimas: ', round(desv_est, 2))
