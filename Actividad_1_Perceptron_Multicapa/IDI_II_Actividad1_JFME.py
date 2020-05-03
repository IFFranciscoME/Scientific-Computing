
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio en Clase con Perceptron Multicapa
# -- codigo: IDI_II_Actividad1_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Leer datos de entrada
datos_excel = pd.read_excel('PercMultAplicado.xlsx')

# datos originales con normalizacion de variables
datos = pd.DataFrame({'x1': datos_excel['Monto']/300000,
                      'x2': datos_excel['Mensualidad']/datos_excel['Ingreso mensual'],
                      'x3': datos_excel['Antigüedad laboral (meses)']/180,
                      'salida': datos_excel['Mora']})

datos['salida'] = [1 if datos['salida'][i] == 'SI' else 0
                   for i in range(0, len(datos['salida']))]

datos = np.array(datos)
datos_test, datos_train = train_test_split(datos, test_size=0.7, shuffle=False)

# --------------------------------------------------------- PERCEPTRON MULTICAPA APLICADO -- #
# --------------------------------------------------------------------------------------- -- #

datos_x_train = datos_train[:, 0:-1]
datos_d_train = datos_train[:, -1:]

datos_x_test = datos_test[:, 0:-1]
datos_d_test = datos_test[:, -1:]

# -- PERCEPTRON MULTICAPA
# [Entradas, Neuronas Ocultas, Salidas, Alfa, Error]
params = [3, 6, 1, 0.55, 1e-12]


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
while error > params[4]:
    print(' ------------ CICLO WHILE ------------ ')
    # ciclo para las q observaciones de entrenamiento
    salidas = list()
    for q in range(len(datos_x_train)):
        # q = 0
        # print(' **** iteracion (Q): ' + str(q) + ' **** ')
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
        salidas.append(y)

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
        error = sum(abs(delta_o))

        # actualizacion de pesos para capa oculta
        w_h = w_h + delta_w_h
        # actualizacion de pesos para capa de salida
        w_o = w_o + delta_w_o
        # verificacion de error

    print('El error es: ' + str(error))

print(' ----- ENTRENAMIENTO terminado -----')

salidas_y_hat = [1 if salidas[i][0][0] >= 0.50 else 0 for i in range(0, len(datos_d_train))]
salidas_y = [int(datos_d_train[i][0]) for i in range(0, len(datos_d_train))]
comparacion = pd.DataFrame({'y': salidas_y, 'y_hat': salidas_y_hat})
cm = confusion_matrix(salidas_y, salidas_y_hat)

# [ 1-1, 1-0]
# [ 0-1, 0-0]

aciertos = (cm[0][0] + cm[1][1])/len(datos_d_train)
print(comparacion)
print(aciertos)

# -- ----------------------------------------------------------------------------- PRUEBA -- #

print(' ----- PRUEBA iniciada -----')
salidas_test = list()
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
    salidas_test.append(y)

salidas_test = [salidas_test[i][0][0] for i in range(0, len(salidas_test))]
salidas_y_hat = [1 if salidas_test[i] >= 0.50 else 0 for i in range(0, len(datos_d_test))]
comparacion = pd.DataFrame({'y': salidas_y, 'y_hat': salidas_y_hat})
cm = confusion_matrix(salidas_y, salidas_y_hat)

# [ 1-1, 1-0]
# [ 0-1, 0-0]

aciertos = (cm[0][0] + cm[1][1])/len(datos_d_test)
print(comparacion)
print(aciertos)
