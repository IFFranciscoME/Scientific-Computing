
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

import numpy as np
import random
import os
import pandas as pd
import matplotlib.pyplot as plt
