
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio con Simulated Annealing - Parte 2
# -- codigo: IDI_II_Tarea_6_SA_P1_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

"""
# 1.- Encuentre el ciclo de valor mínimo. Decida la manera de decrementar la temperatura
# para obtener la mejor respuesta que le sea posible

# Configuraciones utilizadas

# Rutas revisadas

# 2.- Ahora utilice una forma distinta para disminuir la temperatura (con respecto a la
# usada en el inciso anterior). ¿Qué modificación requirió para llegar a la respuesta
# obtenida antes?

# Configuraciones utilizadas

# Rutas revisadas

# 3.- Modifique su código para encontrar el ciclo de valor máximo. De nuevo decida la
# manera de decrementar la temperatura para obtener la mejor respuesta que le sea posible

# Configuraciones utilizadas

# Rutas revisadas

# 4.- ahora suponga que la ruta NO debe de ser cíclica. Encuentre la ruta de valor
# minimo sin importar el punto de inicio y el de final

# Configuraciones utilizadas

# Rutas revisadas

# 5.- Por último, suponga que se fija como lugar de inicio Copenhagen y como destino
# final Lynge. Encuentre la mejor ruta de valor mínimo para este caso.

# Configuraciones utilizadas

# Rutas revisadas

"""

import pandas as pd
import numpy as np
import random
import math
import statistics

# random.seed(2020)
# leer datos de entrada
data = pd.read_excel('archivos/dist.xlsx', sheet_name='54c_test')
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
N = 30000
# T
T = 50
# factor de disminucion para T
factor_t = 0.5
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
# Configuracion: T = 1000  | N = 3  | factor_t = 0.8 | T_iter = T_iter*factor_t
# permutaciones maximas:  201
# rutas revisadas por iteracion:  186
# rutas totales revisadas en  100  iteraciones:  18414
# la ruta con distancia minima:  ['GDL', 'León', 'México', 'Mérida', 'Tapachula',
# 'Monterrey', 'Chihuahua', 'Tijuana', 'GDL']
# distancia de la ruta mínima:  9524
# desviacion estandar de distancias minimas:  276.41

# PRUEBA 2
# -----------------------------------
# Configuracion: T = 1000  | N = 1  | factor_t = 0.9 | T_iter = T_iter*factor_t
# permutaciones maximas:  201
# rutas revisadas por iteracion:  132
# rutas totales revisadas en  100  iteraciones:  13068
# la ruta con distancia minima:  ['León', 'GDL', 'Tijuana', 'Chihuahua', 'Monterrey',
# 'Tapachula', 'Mérida', 'México', 'León']
# distancia de la ruta mínima:  9524
# desviacion estandar de distancias minimas:  350.84

# PRUEBA 3
# -----------------------------------
# Configuracion: T = 1000  | N = 5  | factor_t = 0.7 | T_iter = T_iter*factor_t
# permutaciones maximas:  201
# rutas revisadas por iteracion:  200
# rutas totales revisadas en  100  iteraciones:  19800
# la ruta con distancia minima:  ['México', 'León', 'GDL', 'Tijuana', 'Chihuahua',
# 'Monterrey', 'Tapachula', 'Mérida', 'México']
# distancia de la ruta mínima:  9524
# desviacion estandar de distancias minimas:  288.2

# PRUEBA 4
# -----------------------------------
# Configuracion: T = 1000  | N = 8  | factor_t = 0.99 | T_iter = T_iter*factor_t
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
# Configuracion: T = 1000  | N = 8  | factor_t = 0.99 | T_iter = T_iter*factor_t
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
# Configuracion: T = 1000  | N = 16  | factor_t = 0.9 | T_iter = T_iter*factor_t
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
# Configuracion: T = 500  | N = 16  | factor_t = 0.9 | T_iter = T_iter*factor_t
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
# Configuracion: T = 250  | N = 32  | factor_t = 0.99 | T_iter = T_iter*factor_t
# permutaciones maximas:  12164510040883200
# rutas revisadas por iteracion:  35200
# rutas totales revisadas en  100  iteraciones:  3484800
# la ruta con distancia minima:  ['Ahuisculco', 'Altus Bosques', 'Atequiza', 'Ahuatlán',
# 'Atotonilco el Alto', 'Allende', 'Arandas', 'Acatic', 'Ajijic', 'Atemajac de Brizuela',
# 'Alista', 'Atacco', 'Atengo', 'Acatlán de Juárez', 'Amacueca', 'Atenguillo',
# 'Ahualulco de Mercado', 'Ameca', 'Antonio Escobedo', 'Amatitán', 'Ahuisculco']
# distancia de la ruta mínima:  1560.7740000000001
# desviacion estandar de distancias minimas:  70.4

# PRUEBA 5
# -----------------------------------
# Configuracion: T = 500  | N = 100  | factor_t = 0.99 | T_iter = T_iter/np.log(n_iter)
# permutaciones maximas:  12164510040883200
# rutas revisadas por iteracion:  1000
# rutas totales revisadas en  100  iteraciones:  99000
# la ruta con distancia minima:  ['Ahuisculco', 'Acatlán de Juárez', 'Arandas', 'Allende',
# 'Atotonilco el Alto', 'Ahuatlán', 'Alista', 'Atacco', 'Altus Bosques',
# 'Atemajac de Brizuela', 'Amacueca', 'Acatic', 'Ajijic', 'Atequiza', 'Ahualulco de Mercado',
# 'Antonio Escobedo', 'Atengo', 'Ameca', 'Atenguillo', 'Amatitán', 'Ahuisculco']
# distancia de la ruta mínima:  1808.8590000000002
# desviacion estandar de distancias minimas:  132.58

# PRUEBA 6
# -----------------------------------
# Configuracion: T = 500  | N = 1000  | factor_t = 0.8 | T_iter =
#                                                           math.exp(-factor_t*itera_t)*T_iter
# permutaciones maximas:  12164510040883200
# rutas revisadas por iteracion:  8000
# rutas totales revisadas en  100  iteraciones:  792000
# la ruta con distancia minima:  ['Arandas', 'Allende', 'Ahuatlán', 'Acatic', 'Atequiza',
# 'Ajijic', 'Acatlán de Juárez', 'Ahuisculco', 'Ahualulco de Mercado', 'Antonio Escobedo',
# 'Amatitán', 'Ameca', 'Atenguillo', 'Atengo', 'Alista', 'Atacco', 'Amacueca',
# 'Atemajac de Brizuela', 'Altus Bosques', 'Atotonilco el Alto', 'Arandas']
# distancia de la ruta mínima:  1328.8690000000004
# desviacion estandar de distancias minimas:  111.7

# PRUEBA 7
# -----------------------------------
# Configuracion: T = 50  | N = 20000  | factor_t = 0.8 | T_iter = math.exp(-itera_t)*T_iter
# permutaciones maximas:  12164510040883200
# rutas revisadas por iteracion:  120000
# rutas totales revisadas en  100  iteraciones:  11880000
# la ruta con distancia minima:  ['Atemajac de Brizuela', 'Atacco', 'Alista', 'Atengo',
# 'Atenguillo', 'Ameca', 'Ahualulco de Mercado', 'Antonio Escobedo', 'Amatitán',
# 'Ahuisculco', 'Altus Bosques', 'Acatic', 'Arandas', 'Allende', 'Atotonilco el Alto',
# 'Ahuatlán', 'Atequiza', 'Ajijic', 'Acatlán de Juárez', 'Amacueca', 'Atemajac de Brizuela']
# distancia de la ruta mínima:  1198.693
# desviacion estandar de distancias minimas:  33.05
