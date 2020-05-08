
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Perceptron Simple
# -- codigo: IDI_II_Tarea_7_Perceptron_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

"""

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -- ------------------------------------------------------------------ Datos de entrada -- #
datos = pd.read_excel('archivos/tabla_perceptron.xlsx')
nulos = list(datos['d'].isnull())
train = np.array(datos[[not i for i in nulos]].reset_index(inplace=False, drop=True))
test = np.array(datos[nulos].reset_index(inplace=False, drop=True))

# -- ---------------------------------------------------------------------------- Modelo -- #


class Perceptron():
    """
    Clase para perceptron simple
    """

    def __init__(self, alfa):
        """
        constructor de clase

        Parameters
        ----------
        alfa : float : tasa de aprendizaje

        Return
        ------
        self.alfa = alfa

        """

        self.alfa = alfa

    def sigma(self, x_entradas):
        """
        Para calcular el producto de las entradas por sus pesos.

        Parameters
        ----------
        x_entradas : np.array : datos de entrenamiento con las caracteristicas

        Returns
        -------
        zeta :

        """

        # se utiliza el producto punto
        salida_sigma = np.dot(1, self.pesos[0]) + np.dot(x_entradas, self.pesos[1:])

        return salida_sigma

    def clasificar(self, entradas_clasificar):
        """
        Calcula la salida de la neurona teniendo en cuenta la función de activación

        :param entradas_clasificar: datos con los que predecir la salida de la neurona. Array
        :return: salida de la neurona
        """

        # ajustar a 1 si la salida es mayor o igual a 0, y a 0 para las demas
        # es equivalente al escalon unitario.
        salida_ajustada = np.where(self.sigma(entradas_clasificar) >= 0.0, 1, 0)

        return salida_ajustada

    def entrenar(self, x_entradas, y_salidas):
        """

        Parameters
        ----------
        x_entradas
        y_salidas
        """

        # Inicializar los pesos en cero, en lugar de aleatorios,
        # da resultados mas estables para este ejemplo en particular
        self.pesos = [0] * (x_entradas.shape[1] + 1)
        # para almacenar errores
        self.errores = []
        # contador de iteraciones
        self.iteraciones = 0

        while True:
            errores = 0
            # con zip se puede hacer una compresion de parametros a iterar, se genera
            # una tupla y se itera elemento a elemento en logica de tupla.
            for ajustados, esperados in zip(x_entradas, y_salidas):
                # print('pre-ajustados', ajustados)
                # print('\nesperados', esperados)

                # diferencia entre ajustados y esperados
                delta_pesos = self.alfa * (esperados - self.clasificar(ajustados))
                self.pesos[1:] += delta_pesos * ajustados
                self.pesos[0] += delta_pesos * 1
                # acumular los diferentes de 0 como errores
                errores += int(delta_pesos != 0.0)

                # print('en la iteracion: ', iteraciones, ' los errores son: ', errores)
            self.errores.append(errores)
            self.iteraciones += 1
            # cuando ya no haya errores salir del while
            if errores == 0:
                break


# Instancia de la clase Perceptron
perceptron = Perceptron(alfa=0.1)

# -- ---------------------------------------------------------- Proceso de entrenamiento -- #

# utilizar datos de entrenamiento
perceptron.entrenar(x_entradas=train[0:, :-1], y_salidas=train[0:, -1])

# grafica para apoyo visual
errores = perceptron.errores
plt.plot(range(0, len(errores)), errores, marker='x')
plt.xlabel('No. de iteracion')
# datos de entrada diferentes de salida
plt.ylabel('Errores')
plt.show()

# -- -------------------------------------------------------------- Proceso de validacion -- #
# salidas con las que se entreno train[:, -1]
validacion = perceptron.clasificar(train[:, 0:-1])
df_data_val = pd.DataFrame(train.astype(int), columns=['x0', 'x1', 'x2', 'x3', 'y_train'])
df_data_val['y_val'] = pd.DataFrame(np.vstack(validacion))

# imprimir tabla de validacion de proceso de entrenamiento
print(df_data_val)
# -- -------------------------------------------------------------- Proceso de prediccion -- #
prediccion = perceptron.clasificar(test[:, 0:-1])
test[:, -1] = prediccion
df_test = pd.DataFrame(test.astype(int), columns=['x0', 'x1', 'x2', 'x3', 'y_test'])

# imprimir tabla con resultados finales de datos faltantes en tabla de verdad XOR
print(df_test)
