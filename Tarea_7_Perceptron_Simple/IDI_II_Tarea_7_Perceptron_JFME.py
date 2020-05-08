
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II: Perceptron Simple
# -- codigo: IDI_II_Tarea_7_Perceptron_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

"""
1.- Explica las partes de una neurona artificial

En general, está compuesta por 4 secciones:

1: Entradas
    Aqui están incluidos los datos de entrada, generalmente variables de entrada a través de
    las cuales se pretende que la red neuronal artificial "aprenda". También, en esta sección
    se tienen los pesos sinápticos (o pesos solamente), estos son cifras que pueden tomar
    valores positivos, de 0 o negativos, mediante la manipulación de estos pesos se le da
    "mas importancia" o "menos importancia" a cada dato de entrada en el proceso de
    aprendizaje. Un valor positivo en un peso para una entrada actuará como amplificador de
    la importancia de tal dato para el aprendizaje y ajuste a la salida, e inversamente,
    un valor negativo a un peso tendrá un efecto de atenuador de tal dato.

2: Regla de propagación (Sigma)
    Básicamente es la relación que se le dará a cada neurona con las demás, la regla
    mayormente utilizada es una suma ponderada, es decir, consiste en sumar las entradas
    multiplicando cada una por un peso.

3: Función de activación
    Con base al valor resultante de la etapa anterior, se tiene una función de activación que
    se encarga de devolver una salida a partir de una entrada o conjunto de entradas, la
    entrada es el valor generado por la etapa anterior, y la salida se produce al transformar
    tales entradas mediante una función matemática, las mas común es la sigmoidal, pero
    también está la de arco tangente pero es computacionalmente mas costosa
    que la sigmoidal, por el efecto de la derivada de la función.

4: Salidas
    Esta proporciona el valor o los valores de salida con base a la activación de las neuronas.

2.- ¿Por qué consideramos al Perceptrón una red neuronal offline?

    Por que el perceptrón clasifica cada dato al multiplicar esa entrada por el vector
    de pesos, necesita "ajustar" o "aprender" primero todos esos pesos y lograr un ajuste
    a los datos de salida provistos. Es decir, se considera offline por que necesita primero
    "aprender" de todos los datos que tenga disponibles y hacer esto en un solo "batch" o
    una sola secuencia de repeticiones del proceso de aprendizaje.

    Esto debido a que el propósito dee un proceso offline es que el modelo aprenda la
    dinámica o estructura del fenómeno a través de todos los datos con los cuales se le
    entrena para que lo logre. De tal manera que en un aprendizaje offline, los elementos de
    entrada, su orden y su identidad (salida que generan) es conocida por el proceso que
    lo estará aprendiendo

3.- ¿Qué es alfa en el perceptron y cómo afecta su funcionamiento?

    Podría decirse que es la "tasa de aprendizaje", esta afecta directamente las proporciones
    de cambio en los pesos durante el proceso de entrenamiento, un alfa cercana a 0 provoca
    en cambios menos significativos (o conservadores), mientras que un alfa cercana a 1
    hará que las modificaciones de los pesos sea algo mas significativas (o radicales).

4.- Explica la etapa de aprendizaje y el método que usa para hacerlo.

    Se comienza por la elección de pesos para todas las neuronas, esta elección suele ser
    aleatoria y sólo existen heurísticos como guia, no hay una regla absoluta sobre el
    criterio de inicialización de pesos.

    Se hace con una técnica llamada propagación hacia atras, el principio de esto es que
    se busca ajustar los pesos de las conexiones entre las neuronas de la red en función
    de las diferencias entre los valores de salida que se tienen (objetivo) y los valores de
    salida generados por la red (ajustados). Y la regla de retropropagación es simple,
    para cada neurona en la capa de salida (salida ajustada) se le calcula desviación o
    diferencia respecto a la salida objetivo como un error delta. y este luego se utiliza
    para cambiar los pesos hacia la neurona previa (de ahi retropropagación), como un
    efecto cadena. Uno de los conceptos principales para este proceso es que la propagación
    hacia atrás se hace mediante las derivadas de la función activación respecto a cada
    capa y cada neurona de cada capa hacia atrás.

    Finalmente, un criterio de paro para la retroprogragación es que, dado que los pesos
    de las conexiones entre neuronas se modifican a cada iteración, se puede afirmar que
    este proceso ha terminado cuando los valores de los pesos permanecen estables, es decir
    que las derivadas no están teniendo cambios significativos ya.

5.- Usa un Perceptrón simple con umbral para llenar los valores
    faltantes de la siguiente tabla.

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

print(df_data_val)
# -- -------------------------------------------------------------- Proceso de prediccion -- #
prediccion = perceptron.clasificar(test[:, 0:-1])
test[:, -1] = prediccion
df_test = pd.DataFrame(test.astype(int), columns=['x0', 'x1', 'x2', 'x3', 'y_test'])

print(df_test)
