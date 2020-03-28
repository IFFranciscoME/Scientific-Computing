
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio con Perceptron Multicapa
# -- codigo: IDI_II_Tarea8_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import pandas as pd
import numpy as np

# Leer datos de entrada
datos = pd.read_excel('tabla_para_probar.xlsx')

# Separar datos de entrenamiento y datos de prueba
datos_test = datos[(datos['d1'] == '?') | (datos['d2'] == '?')]
datos_test.reset_index(inplace=True, drop=True)
datos_train = datos[(datos['d1'] != '?') | (datos['d2'] != '?')]
datos_train.reset_index(inplace=True, drop=True)

datos_train_x = np.array(datos_train.iloc[:, 0:-2], dtype=int)
datos_train_d = np.array(datos_train.iloc[:, -2:], dtype=int)

# -- PERCEPTRON MULTICAPA
# [Entradas, Neuronas Ocultas, Salidas, Alfa]
params = [4, 8, 2, 2.5]


# ------------------------------------------------------------------------------- Proceso -- #

def funcion_activacion(param_f, param_x, param_alfa):
    """
    Parameters
    ----------
    param_alfa : float : alfa en la formula
    param_f : str : tipo de funcion de activacion
    param_x : np.array : matriz de neuronas para el calculo

    Returns
    -------
    calculo realizado segun funcion de activacion seleccionada

    Debugging
    ---------
    param_alfa = 2.5
    param_x = net_h

    """
    if param_f == 'sigmoid':
        return 1 / (1 + np.e ** (-param_alfa * param_x))
    else:
        print('funcion no reconocida')


# -- PARAMETROS FIJOS
# matriz de pesos de entrada
w_h = np.array(np.random.random_sample(size=[params[1], params[0]]))
# matriz de pesos de salida
w_o = np.array(np.random.random_sample(size=[params[2], params[1]]))

# -- PARAMETRO A ITERAR
# vector de N entradas
x_j = datos_train_x[0, :][np.newaxis, :]

# -- FORWARD
# red de la capa oculta
net_h = w_h.dot(x_j.T)
# salidas de capa oculta
y_h = funcion_activacion(param_f='sigmoid', param_x=net_h, param_alfa=params[3])
# red de capa de salida
net_o = w_o.dot(y_h)
# salida
y = funcion_activacion(param_f='sigmoid', param_x=net_o, param_alfa=params[3])

# -- BACKWARD
delta_o = np.multiply((datos_train_d[0][np.newaxis, :].T - y), np.multiply(y, (1-y)))
delta_h = np.multiply(np.multiply(y_h, (1-y_h)), w_o.T.dot(delta_o))

delta_w_o = (params[3]*delta_o).dot(y_h.T)
delta_w_h = (params[3]*delta_h).dot(x_j)

error = delta_o
