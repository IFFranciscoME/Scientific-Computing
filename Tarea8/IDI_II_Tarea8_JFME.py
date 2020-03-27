
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio con Perceptron Multicapa
# -- codigo: IDI_II_Tarea8_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import pandas as pd

# Leer datos de entrada
datos = pd.read_excel('tabla_para_probar.xlsx')

# Separar datos de entrenamiento y datos de prueba
datos_prb = datos[(datos['d1'] == '?') | (datos['d2'] == '?')]
datos_prb.reset_index(inplace=True, drop=True)
datos_ent = datos[(datos['d1'] != '?') | (datos['d2'] != '?')]
datos_ent.reset_index(inplace=True, drop=True)
