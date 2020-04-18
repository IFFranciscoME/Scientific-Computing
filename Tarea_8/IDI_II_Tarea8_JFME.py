
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

# -- Entrenamiento
datos_x_train = np.array(datos_train.iloc[:, 0:-2], dtype=int)
datos_d_train = np.array(datos_train.iloc[:, -2:], dtype=int)

# -- PERCEPTRON MULTICAPA
# [Entradas, Neuronas Ocultas, Salidas, Alfa]
params = [4, 8, 1, 2.5]


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


# -- PARAMETROS INICIALES
# matriz de pesos de entrada
w_h = np.array(np.random.random_sample(size=[params[1], params[0]]))
w_h_ini = w_h
# matriz de pesos de salida
w_o = np.array(np.random.random_sample(size=[params[2], params[1]]))
w_o_ini = w_o

# -- ------------------------------------------------------- ITERACIONES DE ENTRENAMIENTO -- #

error = 1
# entrenar hasta lograr pasar un error objetivo
while error > 1e-6:
    # ciclo para las q observaciones de entrenamiento
    for q in range(len(datos_x_train)):
        # q = 0
        print('iteracion (Q): ' + str(q))
        # vector Q de N entradas
        x_j = datos_x_train[q, :][np.newaxis, :]

        # -- FORWARD
        # red de la capa oculta
        net_h = w_h.dot(x_j.T)
        # salidas de capa oculta
        y_h = funcion_activacion(param_f='sigmoid', param_x=net_h, param_alfa=params[3])
        # red de capa de salida
        net_o = w_o.dot(y_h)
        # salida
        y = funcion_activacion(param_f='sigmoid', param_x=net_o, param_alfa=params[3])
        print(y.T)
        # print('d1 = ' + str(round(y[0][0], 2)) + ' | d2 = ' + str(round(y[1][0], 2)))

        # -- BACKWARD
        # errores de la capa de salida
        delta_o = np.multiply((datos_d_train[q][np.newaxis, :].T - y), np.multiply(y, (1-y)))
        # errores de la capa oculta
        delta_h = np.multiply(np.multiply(y_h, (1-y_h)), w_o.T.dot(delta_o))
        # correcciones para pesos de capa de salida
        delta_w_o = (params[3]*delta_o).dot(y_h.T)
        # correcciones para pesos de capa oculta
        delta_w_h = (params[3]*delta_h).dot(x_j)

        # calculo de la cota de error
        error = abs(sum(delta_o))

        # actualizacion de pesos para capa oculta
        w_h = w_h + delta_w_h
        # actualizacion de pesos para capa de salida
        w_o = w_o + delta_w_o
        # verificacion de error
    print('El error es: ' + str(error))

print(' ----- ENTRENAMIENTO terminado -----')

# print('Termino entrenamiento')
# print('los pesos en capa oculta quedaron: ')
# print(w_h)
# print('los pesos en capa de salida quedaron: ')
# print(w_o)

# -- ------------------------------------------------------------- PREDICCION CON PRUEBAS -- #

# -- volver a validar con datos de entrenamiento
datos_x_train = np.array(datos_train.iloc[:, 0:-2], dtype=int)

# -- Prueba
datos_x_test = np.array(datos_test.iloc[:, 0:-2], dtype=int)

print(' ----- PRUEBA iniciada -----')

for q in range(len(datos_x_test)):
    # vector Q de N entradas
    x_j = datos_x_test[q, :][np.newaxis, :]

    # -- FORWARD
    # red de la capa oculta
    net_h = w_h.dot(x_j.T)
    # salidas de capa oculta
    y_h = funcion_activacion(param_f='sigmoid', param_x=net_h, param_alfa=params[3])
    # red de capa de salida
    net_o = w_o.dot(y_h)
    # salida
    y = funcion_activacion(param_f='sigmoid', param_x=net_o, param_alfa=params[3])
    print(y.T)
    # print('d1 = ' + str(round(y[0][0], 2)) + ' | d2 = ' + str(round(y[1][0], 2)))
