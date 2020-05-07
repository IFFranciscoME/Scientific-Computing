
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
data = pd.read_excel('archivos/dist.xlsx', sheet_name='20c_test')
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


# -- Parametros SA
# datos vecinos revisados aleatoriamente
N = 400
# T
T = 300
# factor de disminucion para T
factor_t = 0.99
# --

# para controlar permutaciones maximas
permutaciones = math.factorial(len(np_data[1, :]))/2
perm_max = int(permutaciones*0.01)

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

    # (10) mientras T sea  1 se repetira el proceso
    while T_iter > 1:
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
        T_iter = T_iter*factor_t

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

# ---------------------------------------------------------------------------- SECCION 1 -- #

# PRUEBA 1
# -----------------------------------
# Configuracion: T = 1000  | N = 3  | factor_t = 0.8
# permutaciones maximas:  201
# rutas revisadas por iteracion:  186
# rutas totales revisadas en  100  iteraciones:  18414
# la ruta con distancia minima:  ['GDL', 'León', 'México', 'Mérida', 'Tapachula',
# 'Monterrey', 'Chihuahua', 'Tijuana', 'GDL']
# distancia de la ruta mínima:  9524
# desviacion estandar de distancias minimas:  276.41

# PRUEBA 2
# -----------------------------------
# Configuracion: T = 1000  | N = 1  | factor_t = 0.9
# permutaciones maximas:  201
# rutas revisadas por iteracion:  132
# rutas totales revisadas en  100  iteraciones:  13068
# la ruta con distancia minima:  ['León', 'GDL', 'Tijuana', 'Chihuahua', 'Monterrey',
# 'Tapachula', 'Mérida', 'México', 'León']
# distancia de la ruta mínima:  9524
# desviacion estandar de distancias minimas:  350.84

# PRUEBA 3
# -----------------------------------
# Configuracion: T = 1000  | N = 5  | factor_t = 0.7
# permutaciones maximas:  201
# rutas revisadas por iteracion:  200
# rutas totales revisadas en  100  iteraciones:  19800
# la ruta con distancia minima:  ['México', 'León', 'GDL', 'Tijuana', 'Chihuahua',
# 'Monterrey', 'Tapachula', 'Mérida', 'México']
# distancia de la ruta mínima:  9524
# desviacion estandar de distancias minimas:  288.2

# PRUEBA 4
# -----------------------------------
# Configuracion: T = 1000  | N = 8  | factor_t = 0.99
# permutaciones maximas:  201
# rutas revisadas por iteracion:  11008
# rutas totales revisadas en  100  iteraciones:  1089792
# la ruta con distancia minima:  ['Mérida', 'México', 'León', 'GDL', 'Tijuana',
# 'Chihuahua', 'Monterrey', 'Tapachula', 'Mérida']
# distancia de la ruta mínima:  9524
# desviacion estandar de distancias minimas:  0.0

# ---------------------------------------------------------------------------- SECCION 2 -- #

# PRUEBA 1
# -----------------------------------
# Configuracion: T = 1000  | N = 8  | factor_t = 0.99
# permutaciones maximas:  12164510040883200
# rutas revisadas por iteracion:  11008
# rutas totales revisadas en  100  iteraciones:  1089792
# la ruta con distancia minima:  ['Ahuisculco', 'Amatitán', 'Ahualulco de Mercado',
# 'Atenguillo', 'Atengo', 'Atacco', 'Atemajac de Brizuela', 'Acatlán de Juárez', 'Ameca',
# 'Alista', 'Amacueca', 'Ajijic', 'Atequiza', 'Altus Bosques', 'Acatic', 'Ahuatlán',
# 'Allende', 'Arandas', 'Atotonilco el Alto', 'Antonio Escobedo', 'Ahuisculco']
# distancia de la ruta mínima:  1801.1650000000002
# desviacion estandar de distancias minimas:  94.26

# PRUEBA 2
# -----------------------------------
# Configuracion: T = 1000  | N = 16  | factor_t = 0.9
# permutaciones maximas:  12164510040883200
# rutas revisadas por iteracion:  2112
# rutas totales revisadas en  100  iteraciones:  209088
# la ruta con distancia minima:  ['Ahualulco de Mercado', 'Antonio Escobedo', 'Ajijic',
# 'Ahuisculco', 'Altus Bosques', 'Acatic', 'Atotonilco el Alto', 'Arandas', 'Allende',
# 'Alista', 'Atemajac de Brizuela', 'Atacco', 'Amacueca', 'Atequiza', 'Ahuatlán',
# 'Acatlán de Juárez', 'Atengo', 'Atenguillo', 'Amatitán', 'Ameca', 'Ahualulco de Mercado']
# distancia de la ruta mínima:  1775.4059999999997
# desviacion estandar de distancias minimas:  125.14

# PRUEBA 3
# -----------------------------------
# Configuracion: T = 500  | N = 16  | factor_t = 0.9
# permutaciones maximas:  12164510040883200
# rutas revisadas por iteracion:  1888
# rutas totales revisadas en  100  iteraciones:  186912
# la ruta con distancia minima:  ['Ahualulco de Mercado', 'Amatitán', 'Altus Bosques',
# 'Atotonilco el Alto', 'Allende', 'Arandas', 'Ahuatlán', 'Ajijic', 'Amacueca',
# 'Atemajac de Brizuela', 'Atacco', 'Alista', 'Atequiza', 'Acatic', 'Ahuisculco', 'Ameca',
# 'Acatlán de Juárez', 'Atengo', 'Atenguillo', 'Antonio Escobedo', 'Ahualulco de Mercado']
# distancia de la ruta mínima:  1669.1289999999997
# desviacion estandar de distancias minimas:  124.88

# PRUEBA 4
# -----------------------------------
# Configuracion: T = 250  | N = 32  | factor_t = 0.99
# permutaciones maximas:  12164510040883200
# rutas revisadas por iteracion:  35200
# rutas totales revisadas en  100  iteraciones:  3484800
# la ruta con distancia minima:  ['Ahuisculco', 'Altus Bosques', 'Atequiza', 'Ahuatlán',
# 'Atotonilco el Alto', 'Allende', 'Arandas', 'Acatic', 'Ajijic', 'Atemajac de Brizuela',
# 'Alista', 'Atacco', 'Atengo', 'Acatlán de Juárez', 'Amacueca', 'Atenguillo',
# 'Ahualulco de Mercado', 'Ameca', 'Antonio Escobedo', 'Amatitán', 'Ahuisculco']
# distancia de la ruta mínima:  1560.7740000000001
# desviacion estandar de distancias minimas:  70.4

# PRUEBA 5 (Tardó aprox 20 mins)
# -----------------------------------
# Configuracion: T = 300  | N = 400  | factor_t = 0.99
# permutaciones maximas:  12164510040883200
# rutas revisadas por iteracion:  454400
# rutas totales revisadas en  100  iteraciones:  44985600
# la ruta con distancia minima:  ['Atengo', 'Atenguillo', 'Amatitán', 'Ameca',
# 'Antonio Escobedo', 'Ahuisculco', 'Arandas', 'Allende', 'Atotonilco el Alto',
# 'Ahuatlán', 'Acatic', 'Altus Bosques', 'Acatlán de Juárez', 'Amacueca', 'Atacco',
# 'Alista', 'Atemajac de Brizuela', 'Atequiza', 'Ajijic', 'Ahualulco de Mercado', 'Atengo']
# distancia de la ruta mínima:  1536.8429999999998
# desviacion estandar de distancias minimas:  54.54
