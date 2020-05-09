
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Ejercicio con Perceptron Multicapa
# -- codigo: Script_Question_12.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Leer datos de entrada
datos = pd.read_excel('Question_12/Question_12.xlsx', sheet_name='datos')

# Separar datos de entrenamiento y datos de prueba
datos_train = datos[datos['y'] != '?']*10
datos_train.reset_index(inplace=True, drop=True)

datos_test = datos[datos['y'] == '?']*10
datos_test.reset_index(inplace=True, drop=True)

# -- Entrenamiento
datos_x = np.array(pd.DataFrame(datos_train.iloc[:, 0])).astype('float64')
datos_d = np.array(pd.DataFrame(datos_train.iloc[:, 1])).astype('float64')

# -- PERCEPTRON MULTICAPA
# [Entradas, Neuronas Ocultas, Salidas, Alfa]
params = [1, 1, 1, 3.5]


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
    print('\n')
    print(' ----- Entrenamiento terminado -----')
    for q in range(len(datos_x)):
        # q = 0
        print('iteracion (Q): ' + str(q))

        # vector Q de N entradas
        x_j = datos_x[q, :][np.newaxis, :]

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
        # print('y = ' + str(y))

        # -- BACKWARD
        # errores de la capa de salida
        delta_o = np.multiply((datos_d[q][np.newaxis, :].T - y), np.multiply(y, (1-y)))
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
    print('da un error de: ' + str(error))

# print('\n')
# print('Termino entrenamiento')
# print('los pesos en capa oculta quedaron: ')
# print(w_h)
# print('los pesos en capa de salida quedaron: ')
# print(w_o)


# -- ------------------------------------------------------------- PREDICCION CON PRUEBAS -- #

# -- Prueba
# datos_x = np.array(pd.DataFrame(df_data['test_x']).iloc[:, 0:-3], dtype=int)
datos_d = np.array(pd.DataFrame(datos_test.iloc[:, 0])).astype(float)

for q in range(len(datos_x)):
    # vector Q de N entradas
    x_j = datos_x[q, :][np.newaxis, :]

    # -- FORWARD
    # red de la capa oculta
    net_h = w_h.dot(x_j.T)
    # salidas de capa oculta
    y_h = funcion_activacion(param_f='sigmoid', param_x=net_h, param_alfa=params[3])
    # red de capa de salida
    net_o = w_o.dot(y_h)
    # salida
    y = funcion_activacion(param_f='sigmoid', param_x=net_o, param_alfa=params[3])
    # print(y.T)
    print('d1 = ' + str(round(y[0][0], 2)))

    # -- BACKWARD
    # errores de la capa de salida
    delta_o = np.multiply((datos_d[q][np.newaxis, :].T - y), np.multiply(y, (1-y)))
    # errores de la capa oculta
    delta_h = np.multiply(np.multiply(y_h, (1-y_h)), w_o.T.dot(delta_o))
    # correcciones para pesos de capa de salida
    delta_w_o = (params[3]*delta_o).dot(y_h.T)
    # correcciones para pesos de capa oculta
    delta_w_h = (params[3]*delta_h).dot(x_j)

    # calculo de la cota de error
    error = abs(sum(delta_o))


# -- ---------------------------------------------------------------------- MODELO LINEAL -- #

x = np.array(pd.DataFrame(datos_train.iloc[:, 0])).astype('float64')
x_new = np.array(pd.DataFrame(datos_test.iloc[:, 0])).astype('float64')
y = np.array(pd.DataFrame(datos_train.iloc[:, 1])).astype('float64')
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
m = model.coef_[0]
b = model.intercept_
print('ECUACION: y = {0} * x + {1}'.format(m[0], b[0]))

y_pred = model.intercept_ + model.coef_ * x_new
print('Pronostico:', y_pred, sep='\n')
