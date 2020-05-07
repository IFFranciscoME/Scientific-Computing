
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio con Simulated Annealing - Parte 2
# -- codigo: IDI_II_Tarea_6_SA_P1_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import pandas as pd
import numpy as np
import random
import math
import statistics

# random.seed(2020)
# leer datos de entrada
data = pd.read_excel('archivos/54c_test.xlsx', sheet_name='54c_test')
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
N = 1680
# T
T = 25
# factor de disminucion para T
factor_t = 0.80
# --

# para controlar permutaciones maximas
permutaciones = math.factorial(len(np_data[1, :]))/2
perm_max = int(permutaciones*0.01)

# -- ----------------------------------------------------------------------------- SA -- #
for j in range(0, n_corridas):
    # j = 0

    # contador para permutaciones maximas
    contador = 0

    # -- Para ejercicio 5
    # Inicio: Copenhagen | Fin: lynge
    # ciudad_inicio = list(ciudades).index('Copenhagen')
    # ciudad_fin = list(ciudades).index('Lynge')

    # configuracion inicial aleatoria
    recorrido_rand = list(np.arange(len(np_data[:, 0])))
    random.shuffle(recorrido_rand)
    C1 = recorrido_rand

    # -- Para ejercicio 5
    # C1.remove(ciudad_inicio)
    # C1.remove(ciudad_fin)
    # C1.insert(0, ciudad_inicio)
    # C1.append(ciudad_fin)

    # hacer ciclica o no ciclica la ruta
    # agregar primer numero al ultimo para C1 y para C2
    # C1.append(C1[0])

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

            # Para ruta ciclica
            ind_C1 = np.arange(1, len(C1)-1)

            # para ruta no ciclica
            # ind_C1 = np.arange(0, len(C1))

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

            # para que busque el minimo
            q = math.e ** ((E1 - E2) / T)

            # para que busque el maximo
            # q = math.e ** ((E2 - E1) / T)

            # (p6 y p7) aceptar o rechazar aleatoriamente la config de parametros nueva
            p = np.random.random(1)[0]
            if p < q:
                C1 = C2

            # p(11) guardar en lista el valor de la configuracion actual
            rutas.append(C1)
            # lista de distancias totales por ruta
            distancias.append(sum([np_data[C1[i]][C1[i+1]] for i in range(0, len(C1)-1)]))

        # 9.- Disminuya en 10% el valor de T

        # print(itera_t)
        # (1)
        T_iter = T_iter*factor_t

        # (2)
        # T_iter = T_iter/np.log(n_iter)

        # (3)
        # T_iter = math.exp(-itera_t)*T_iter

# -- ------------------------------------------------------------------------ PARA MAXIMO -- #
#     print('\n corrida numero = ', j)
#     id_distancia_maxima = np.argmax(distancias)
#     distancia_maxima = np.argmax(distancias)
#     print('permutaciones maximas: ', perm_max)
#     print('permutaciones hechas: ', contador)
#     print('distancia maxima encontrada: ', distancias[distancia_maxima])
#     ruta_distancia_maxima = rutas[distancia_maxima]
#     ciudades = list(ciudades)
#     recorrido = [ciudades[ruta_distancia_maxima[c]] for c in range(0, len(ciudades)+1)]
#     print('el recorrido fue: ', recorrido)
#
#     distancias_varias.append(distancias[distancia_maxima])
#     rutas_varias.append(recorrido)
#
# desv_est = statistics.stdev(distancias_varias)
# print('\n \n----------------------------------- ')
# print('Configuracion: ' 'T =', T, ' | N =', N, ' | factor_t =', factor_t)
# print('permutaciones maximas: ', perm_max)
# print('rutas revisadas por iteracion: ', contador)
# print('rutas totales revisadas en ', j+1, ' iteraciones: ', contador*j)
# print('la ruta con distancia maxima: ', rutas_varias[np.argmax(distancias_varias)])
# print('distancia de la ruta maxima: ', distancias_varias[np.argmax(distancias_varias)])
# print('desviacion estandar de distancias maximas: ', round(desv_est, 2))

# -- ---------------------------------------------------------------------- PARA MINIMO -- #
    print('\n corrida numero = ', j)
    id_distancia_minima = np.argmin(distancias)
    distancia_minima = np.argmin(distancias)
    print('permutaciones maximas: ', perm_max)
    print('permutaciones hechas: ', contador)
    print('distancia minima encontrada: ', distancias[distancia_minima])
    ruta_distancia_minima = rutas[distancia_minima]
    ciudades = list(ciudades)
    recorrido = [ciudades[ruta_distancia_minima[c]] for c in range(0, len(ciudades)+1)]

    # Ejercicio 5
    # recorrido = [ciudades[ruta_distancia_minima[c]] for c in range(0, len(ciudades))]

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

# ------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------ #
# 1.- Encuentre el ciclo de valor mínimo. Decida la manera de decrementar la temperatura
# para obtener la mejor respuesta que le sea posible
# ------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------ #

# -- Configuraciones utilizadas
# CONFIGURACION 1
# -----------------------------------
# Configuracion: T = 50  | N = 280  | factor_t = 0.8 | T_iter = T_iter*factor_t
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  10080
# rutas totales revisadas en  100  iteraciones:  997920

# la ruta con distancia minima:  ['Værløse', 'Måløv', 'Slangerup', 'Hillerød', 'Lynge',
# 'Stenløse', 'Ishøj', 'Dragør', 'Christianshavn', 'Tårnby', 'Vallensbæk', 'Rødovre',
# 'Hvidovre', 'Hørsholm', 'Birkerød', 'Glostrup', 'Fløng', 'Skibby', 'Hornbæk', 'Hellebæk',
# 'Humlebæk', 'Stavnsholt', 'Helsingør', 'Blovstrød', 'Frederiksværk', 'Skævinge',
# 'Espergærde', 'Græsted', 'Helsinge', 'Liseleje', 'Fredensborg', 'Frederiksberg',
# 'Lillerød', 'Veksø', 'Charlottenlund', 'Copenhagen', 'Taastrup', 'Ballerup', 'Albertslund',
# 'Gilleleje', 'Nivå', 'Nødebo', 'Kongens Lyngby', 'Ølstykke', 'Ganløse', 'Hundested',
# 'Jægerspris', 'Frederikssund', 'Trørød', 'Farum', 'Åkirkeby', 'Nexø', 'Rønne',
# 'Smørumnedre', 'Værløse']

# distancia de la ruta mínima:  964.32771506
# desviacion estandar de distancias minimas:  30.6

# ------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------ #
# 2.- Ahora utilice una forma distinta para disminuir la temperatura (con respecto a la
# usada en el inciso anterior). ¿Qué modificación requirió para llegar a la respuesta
# obtenida antes? :
# ------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------ #

# CONFIGURACION 2
# -----------------------------------
# Configuracion: T = 25  | N = 1120  | factor_t = 0.8 | T_iter = T_iter/np.log(n_iter)
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  4480
# rutas totales revisadas en  100  iteraciones:  443520

# la ruta con distancia minima:  ['Ballerup', 'Ganløse', 'Stavnsholt', 'Trørød', 'Rødovre',
# 'Værløse', 'Jægerspris', 'Hillerød', 'Veksø', 'Smørumnedre', 'Glostrup', 'Ishøj', 'Måløv',
# 'Kongens Lyngby', 'Ølstykke', 'Copenhagen', 'Nexø', 'Åkirkeby', 'Rønne', 'Christianshavn',
# 'Hvidovre', 'Tårnby', 'Dragør', 'Skævinge', 'Fredensborg', 'Hellebæk', 'Hornbæk', 'Nødebo',
# 'Lynge', 'Farum', 'Græsted', 'Gilleleje', 'Espergærde', 'Nivå', 'Helsingør', 'Humlebæk',
# 'Frederiksberg', 'Blovstrød', 'Skibby', 'Albertslund', 'Vallensbæk', 'Fløng', 'Taastrup',
# 'Birkerød', 'Stenløse', 'Hørsholm', 'Frederikssund', 'Slangerup', 'Lillerød', 'Helsinge',
# 'Frederiksværk', 'Liseleje', 'Hundested', 'Charlottenlund', 'Ballerup']

# distancia de la ruta mínima:  901.1319005799999
# desviacion estandar de distancias minimas:  55.35

# CONFIGURACION 3
# -----------------------------------
# Configuracion: T = 25  | N = 1400  | factor_t = 0.8 | T_iter = T_iter/np.log(n_iter)
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  5600
# rutas totales revisadas en  100  iteraciones:  554400

# la ruta con distancia minima:  ['Farum', 'Veksø', 'Ølstykke', 'Taastrup', 'Ishøj',
# 'Rødovre', 'Fredensborg', 'Hørsholm', 'Liseleje', 'Fløng', 'Hvidovre', 'Lynge',
# 'Jægerspris', 'Skibby', 'Frederiksværk', 'Hundested', 'Helsinge', 'Hornbæk', 'Skævinge',
# 'Slangerup', 'Måløv', 'Kongens Lyngby', 'Stavnsholt', 'Græsted', 'Gilleleje',
# 'Humlebæk', 'Birkerød', 'Copenhagen', 'Nivå', 'Hellebæk', 'Espergærde', 'Helsingør',
# 'Nødebo', 'Hillerød', 'Frederikssund', 'Ganløse', 'Smørumnedre', 'Blovstrød', 'Værløse',
# 'Albertslund', 'Åkirkeby', 'Nexø', 'Rønne', 'Dragør', 'Christianshavn', 'Charlottenlund',
# 'Trørød', 'Frederiksberg', 'Tårnby', 'Stenløse', 'Ballerup', 'Lillerød', 'Glostrup',
# 'Vallensbæk', 'Farum']

# distancia de la ruta mínima:  895.9235772400002
# desviacion estandar de distancias minimas:  47.77

# CONFIGURACION 4
# -----------------------------------
# Configuracion: T = 25  | N = 1680  | factor_t = 0.8 | T_iter = T_iter/np.log(n_iter)
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  6720
# rutas totales revisadas en  100  iteraciones:  665280

# la ruta con distancia minima:  ['Skævinge', 'Ølstykke', 'Farum', 'Hørsholm',
# 'Kongens Lyngby', 'Rødovre', 'Copenhagen', 'Christianshavn', 'Tårnby', 'Lynge',
# 'Veksø', 'Ishøj', 'Nexø', 'Åkirkeby', 'Rønne', 'Taastrup', 'Dragør', 'Charlottenlund',
# 'Slangerup', 'Hundested', 'Skibby', 'Frederiksværk', 'Liseleje', 'Hillerød', 'Nivå',
# 'Græsted', 'Fredensborg', 'Birkerød', 'Nødebo', 'Espergærde', 'Helsingør', 'Hellebæk',
# 'Hornbæk', 'Gilleleje', 'Trørød', 'Lillerød', 'Helsinge', 'Humlebæk', 'Ganløse',
# 'Blovstrød', 'Stenløse', 'Jægerspris', 'Smørumnedre', 'Måløv', 'Glostrup', 'Albertslund',
# 'Vallensbæk', 'Hvidovre', 'Ballerup', 'Fløng', 'Frederikssund', 'Stavnsholt',
# 'Frederiksberg', 'Værløse', 'Skævinge']

# distancia de la ruta mínima:  870.0230115300001
# desviacion estandar de distancias minimas:  36.48

# CONFIGURACION 5
# -----------------------------------
# Configuracion: T = 25  | N = 1680  | factor_t = 0.8 |  T_iter = math.exp(-itera_t)*T_iter
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  10080
# rutas totales revisadas en  100  iteraciones:  997920

# la ruta con distancia minima:  ['Nivå', 'Humlebæk', 'Charlottenlund', 'Trørød',
# 'Kongens Lyngby', 'Hundested', 'Liseleje', 'Stenløse', 'Frederikssund', 'Stavnsholt',
# 'Værløse', 'Farum', 'Jægerspris', 'Helsingør', 'Hellebæk', 'Græsted', 'Ølstykke',
# 'Skævinge', 'Veksø', 'Smørumnedre', 'Slangerup', 'Skibby', 'Hillerød', 'Nødebo',
# 'Fredensborg', 'Hornbæk', 'Espergærde', 'Frederiksværk', 'Gilleleje', 'Helsinge',
# 'Lillerød', 'Birkerød', 'Christianshavn', 'Ishøj', 'Hvidovre', 'Frederiksberg',
# 'Taastrup', 'Måløv', 'Vallensbæk', 'Copenhagen', 'Ballerup', 'Blovstrød', 'Lynge',
# 'Hørsholm', 'Albertslund', 'Rødovre', 'Rønne', 'Åkirkeby', 'Nexø', 'Dragør', 'Tårnby',
# 'Glostrup', 'Fløng', 'Ganløse', 'Nivå']

# distancia de la ruta mínima:  869.15122942
# desviacion estandar de distancias minimas:  26.29

# ------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------ #
# 3.- Modifique su código para encontrar el ciclo de valor máximo. De nuevo decida la
# manera de decrementar la temperatura para obtener la mejor respuesta que le sea posible
# ------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------ #

# CONFIGURACION 1
# -----------------------------------
# Configuracion: T = 50  | N = 280  | factor_t = 0.8 | T_iter = T_iter*factor_t
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  10080
# rutas totales revisadas en  100  iteraciones:  997920

# la ruta con distancia maxima:  ['Fredensborg', 'Rødovre', 'Nødebo', 'Dragør', 'Hundested',
# 'Hvidovre', 'Helsingør', 'Værløse', 'Slangerup', 'Copenhagen', 'Skævinge', 'Frederiksberg',
# 'Humlebæk', 'Kongens Lyngby', 'Hillerød', 'Rønne', 'Blovstrød', 'Hellebæk', 'Taastrup',
# 'Ganløse', 'Åkirkeby', 'Hornbæk', 'Ballerup', 'Stavnsholt', 'Glostrup', 'Græsted', 'Nexø',
# 'Helsinge', 'Skibby', 'Charlottenlund', 'Jægerspris', 'Trørød', 'Smørumnedre', 'Fløng',
# 'Birkerød', 'Lillerød', 'Hørsholm', 'Frederiksværk', 'Ishøj', 'Lynge', 'Måløv',
# 'Frederikssund', 'Tårnby', 'Liseleje', 'Christianshavn', 'Farum', 'Gilleleje',
# 'Albertslund', 'Espergærde', 'Stenløse', 'Vallensbæk', 'Ølstykke', 'Nivå', 'Veksø',
# 'Fredensborg']

# distancia de la ruta maxima:  2112.2783429300002
# desviacion estandar de distancias maximas:  20.5

# CONFIGURACION 2
# -----------------------------------
# Configuracion: T = 25  | N = 1680  | factor_t = 0.8 | T_iter = T_iter/np.log(n_iter)
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  6720
# rutas totales revisadas en  100  iteraciones:  665280

# la ruta con distancia maxima:  ['Copenhagen', 'Ganløse', 'Helsingør', 'Veksø', 'Nivå',
# 'Vallensbæk', 'Slangerup', 'Åkirkeby', 'Skibby', 'Lynge', 'Hvidovre', 'Jægerspris',
# 'Hørsholm', 'Værløse', 'Frederikssund', 'Ishøj', 'Birkerød', 'Christianshavn', 'Stenløse',
# 'Fredensborg', 'Kongens Lyngby', 'Albertslund', 'Humlebæk', 'Rødovre', 'Liseleje',
# 'Frederiksberg', 'Helsinge', 'Dragør', 'Nødebo', 'Glostrup', 'Skævinge', 'Rønne',
# 'Hornbæk', 'Smørumnedre', 'Lillerød', 'Ballerup', 'Gilleleje', 'Taastrup', 'Hellebæk',
# 'Stavnsholt', 'Hundested', 'Nexø', 'Farum', 'Tårnby', 'Måløv', 'Blovstrød', 'Ølstykke',
# 'Espergærde', 'Fløng', 'Græsted', 'Charlottenlund', 'Hillerød', 'Trørød', 'Frederiksværk',
# 'Copenhagen']

# distancia de la ruta maxima:  2151.12266711
# desviacion estandar de distancias maximas:  19.3

# CONFIGURACION 3
# -----------------------------------
# Configuracion: T = 25  | N = 1680  | factor_t = 0.8 | T_iter = math.exp(-itera_t)*T_iter
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  10080
# rutas totales revisadas en  100  iteraciones:  997920

# la ruta con distancia maxima:  ['Kongens Lyngby', 'Rødovre', 'Nivå', 'Slangerup',
# 'Albertslund', 'Hundested', 'Charlottenlund', 'Hillerød', 'Åkirkeby', 'Græsted', 'Tårnby',
# 'Stavnsholt', 'Trørød', 'Liseleje', 'Glostrup', 'Blovstrød', 'Jægerspris', 'Værløse',
# 'Ølstykke', 'Gilleleje', 'Stenløse', 'Copenhagen', 'Birkerød', 'Taastrup', 'Espergærde',
# 'Farum', 'Ishøj', 'Skibby', 'Christianshavn', 'Frederiksværk', 'Rønne', 'Nødebo',
# 'Hvidovre', 'Skævinge', 'Vallensbæk', 'Helsingør', 'Ganløse', 'Dragør', 'Fredensborg',
# 'Nexø', 'Lynge', 'Ballerup', 'Hellebæk', 'Smørumnedre', 'Hornbæk', 'Veksø', 'Lillerød',
# 'Frederiksberg', 'Måløv', 'Humlebæk', 'Fløng', 'Hørsholm', 'Frederikssund', 'Helsinge',
# 'Kongens Lyngby']

# distancia de la ruta maxima:  2138.82140522
# desviacion estandar de distancias maximas:  15.21

# ------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------ #
# 4.- ahora suponga que la ruta NO debe de ser cíclica. Encuentre la ruta de valor
# minimo sin importar el punto de inicio y el de final
# ------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------ #

# CONFIGURACION 1
# -----------------------------------
# Configuracion: T = 50  | N = 280  | factor_t = 0.8 | T_iter = T_iter*factor_t
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  10080
# rutas totales revisadas en  100  iteraciones:  997920

# la ruta con distancia minima:  ['Hellebæk', 'Dragør', 'Lillerød', 'Fredensborg',
# 'Kongens Lyngby', 'Charlottenlund', 'Rødovre', 'Christianshavn', 'Copenhagen', 'Veksø',
# 'Hundested', 'Græsted', 'Blovstrød', 'Lynge', 'Smørumnedre', 'Farum', 'Albertslund',
# 'Ganløse', 'Frederikssund', 'Nivå', 'Stavnsholt', 'Glostrup', 'Nødebo', 'Helsinge',
# 'Humlebæk', 'Skævinge', 'Frederiksværk', 'Liseleje', 'Espergærde', 'Hillerød',
# 'Jægerspris', 'Trørød', 'Hornbæk', 'Gilleleje', 'Helsingør', 'Hørsholm', 'Frederiksberg',
# 'Hvidovre', 'Ballerup', 'Skibby', 'Stenløse', 'Ølstykke', 'Taastrup', 'Værløse',
# 'Birkerød', 'Smørumnedre', 'Måløv', 'Ishøj', 'Vallensbæk', 'Fløng', 'Slangerup',
# 'Tårnby', 'Rønne', 'Åkirkeby', 'Nexø']

# distancia de la ruta mínima:  875.2959573500001
# desviacion estandar de distancias minimas:  52.16

# CONFIGURACION 2
# -----------------------------------
# Configuracion: T = 25  | N = 1120  | factor_t = 0.8 | T_iter = T_iter/np.log(n_iter)
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  4480
# rutas totales revisadas en  100  iteraciones:  443520

# la ruta con distancia minima:  ['Stavnsholt', 'Espergærde', 'Liseleje', 'Græsted',
# 'Frederiksværk', 'Farum', 'Trørød', 'Frederiksberg', 'Christianshavn', 'Albertslund',
# 'Måløv', 'Jægerspris', 'Frederikssund', 'Slangerup', 'Rødovre', 'Veksø', 'Ishøj',
# 'Ballerup', 'Smørumnedre', 'Hundested', 'Skævinge', 'Skibby', 'Vallensbæk', 'Taastrup',
# 'Stenløse', 'Ølstykke', 'Lynge', 'Fløng', 'Dragør', 'Tårnby', 'Gilleleje', 'Helsingør',
# 'Helsinge', 'Nødebo', 'Ganløse', 'Charlottenlund', 'Hørsholm', 'Hillerød', 'Blovstrød',
# 'Birkerød', 'Værløse', 'Fredensborg', 'Hellebæk', 'Hornbæk', 'Kongens Lyngby', 'Humlebæk',
# 'Nivå', 'Lillerød', 'Glostrup', 'Copenhagen', 'Hvidovre', 'Åkirkeby', 'Rønne', 'Åkirkeby',
# 'Nexø']

# distancia de la ruta mínima:  836.4385844
# desviacion estandar de distancias minimas:  59.63

# CONFIGURACION 3
# -----------------------------------
# Configuracion: T = 25  | N = 1680  | factor_t = 0.8 |  T_iter = math.exp(-itera_t)*T_iter
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  10080
# rutas totales revisadas en  100  iteraciones:  997920

# la ruta con distancia minima:  ['Nexø', 'Åkirkeby', 'Rønne', 'Nivå', 'Ishøj',
# 'Frederiksberg', 'Farum', 'Trørød', 'Smørumnedre', 'Ballerup', 'Værløse', 'Taastrup',
# 'Fløng', 'Tårnby', 'Hellebæk', 'Hillerød', 'Stavnsholt', 'Dragør', 'Copenhagen',
# 'Birkerød', 'Stenløse', 'Charlottenlund', 'Skibby', 'Skævinge', 'Nødebo', 'Hørsholm',
# 'Humlebæk', 'Rødovre', 'Hvidovre', 'Christianshavn', 'Christianshavn', 'Lillerød',
# 'Kongens Lyngby', 'Fredensborg', 'Hornbæk', 'Græsted', 'Gilleleje', 'Blovstrød',
# 'Espergærde', 'Helsingør', 'Liseleje', 'Hundested', 'Frederiksværk', 'Jægerspris',
# 'Frederikssund', 'Ølstykke', 'Slangerup', 'Ganløse', 'Veksø', 'Helsinge', 'Lynge',
# 'Måløv', 'Glostrup', 'Vallensbæk', 'Albertslund']

# distancia de la ruta mínima:  812.25734948
# desviacion estandar de distancias minimas:  52.09

# ------------------------------------------------------------------------------------------ #
# 5.- Por último, suponga que se fija como lugar de inicio Copenhagen y como destino
# final Lynge. Encuentre la mejor ruta de valor mínimo para este caso.

# Configuraciones utilizadas

# CONFIGURACION 1
# -----------------------------------
# Configuracion: T = 25  | N = 280  | factor_t = 0.8 | T_iter = T_iter*factor_t
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  8400
# rutas totales revisadas en  100  iteraciones:  831600

# la ruta con distancia minima:  ['Copenhagen', 'Dragør', 'Rønne', 'Nexø', 'Åkirkeby',
# 'Vallensbæk', 'Fløng', 'Glostrup', 'Ishøj', 'Værløse', 'Hvidovre', 'Tårnby',
# 'Charlottenlund', 'Ballerup', 'Helsingør', 'Kongens Lyngby', 'Christianshavn',
# 'Trørød', 'Helsinge', 'Humlebæk', 'Fredensborg', 'Ganløse', 'Nivå', 'Hellebæk',
# 'Nødebo', 'Frederiksværk', 'Hundested', 'Liseleje', 'Espergærde', 'Stavnsholt',
# 'Blovstrød', 'Hørsholm', 'Ølstykke', 'Slangerup', 'Skibby', 'Hillerød', 'Hornbæk'
# , 'Græsted', 'Birkerød', 'Farum', 'Frederiksberg', 'Taastrup', 'Albertslund', 'Smørumnedre',
# 'Stenløse', 'Rødovre', 'Måløv', 'Lillerød', 'Gilleleje', 'Skævinge', 'Veksø',
# 'Frederikssund', 'Jægerspris', 'Lynge']

# distancia de la ruta mínima:  887.0889385799996
# desviacion estandar de distancias minimas:  24.88

# CONFIGURACION 2
# -----------------------------------
# Configuracion: T = 25  | N = 1680  | factor_t = 0.8
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  6720
# rutas totales revisadas en  100  iteraciones:  665280

# la ruta con distancia minima:  ['Copenhagen', 'Hornbæk', 'Gilleleje', 'Humlebæk', 'Nivå',
# 'Lillerød', 'Birkerød', 'Nødebo', 'Helsingør', 'Trørød', 'Hellebæk', 'Hvidovre', 'Ishøj',
# 'Vallensbæk', 'Tårnby', 'Rønne', 'Åkirkeby', 'Nexø', 'Christianshavn', 'Dragør',
# 'Albertslund', 'Smørumnedre', 'Farum', 'Helsinge', 'Liseleje', 'Jægerspris', 'Stenløse',
# 'Glostrup', 'Kongens Lyngby', 'Hørsholm', 'Fredensborg', 'Espergærde', 'Frederiksberg',
# 'Rødovre', 'Veksø', 'Ballerup', 'Værløse', 'Slangerup', 'Hundested', 'Græsted', 'Hillerød',
# 'Frederikssund', 'Ganløse', 'Måløv', 'Ølstykke', 'Skibby', 'Taastrup', 'Fløng',
# 'Charlottenlund', 'Stavnsholt', 'Blovstrød', 'Skævinge', 'Frederiksværk', 'Lynge']

# distancia de la ruta mínima:  870.0547014
# desviacion estandar de distancias minimas:  29.45

# CONFIGURACION 3
# -----------------------------------
# Configuracion: T = 25  | N = 1680  | factor_t = 0.8 | T_iter = math.exp(-itera_t)*T_iter
# permutaciones maximas: 1154218486696206988168326647254666929013545553846695839913173988671488
# rutas revisadas por iteracion:  10080
# rutas totales revisadas en  100  iteraciones:  997920

# la ruta con distancia minima:  ['Copenhagen', 'Veksø', 'Fløng', 'Tårnby', 'Rønne',
# 'Åkirkeby', 'Nexø', 'Rødovre', 'Hvidovre', 'Christianshavn', 'Lillerød', 'Hundested',
# 'Ølstykke', 'Måløv', 'Smørumnedre', 'Hillerød', 'Ishøj', 'Taastrup', 'Dragør', 'Vallensbæk',
# 'Kongens Lyngby', 'Ballerup', 'Blovstrød', 'Fredensborg', 'Nødebo', 'Græsted', 'Espergærde',
# 'Gilleleje', 'Helsinge', 'Helsingør', 'Hornbæk', 'Humlebæk', 'Skibby', 'Skævinge',
# 'Liseleje', 'Frederikssund', 'Frederiksværk', 'Stenløse', 'Ganløse', 'Værløse', 'Trørød',
# 'Albertslund', 'Charlottenlund', 'Jægerspris', 'Slangerup', 'Glostrup', 'Frederiksberg',
# 'Hørsholm', 'Nivå', 'Hellebæk', 'Birkerød', 'Stavnsholt', 'Farum', 'Lynge']

# distancia de la ruta mínima:  893.0087305700001
# desviacion estandar de distancias minimas:  25.28
