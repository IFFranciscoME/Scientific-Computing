
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II
# -- codigo: IDI_II_Tarea3_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

"""
Realice codigo en Python que, recibiendo un sistema de n ecuaciones no lineales
fi(x1, x2, ... , xn) = 0, un valor inicial x=0 y una exactitud (error) dado E,
use el metodo de Newton multivariable para encontrar (si existe) una solucion real del sistema.
Asegurese que cuenta el numero de iteraciones realizadas.

Use su codigo para encontrar (si existe) todas las soluciones reales de cada sistema con
presición de 4 dígitos y exactitud de 10^-3. Puede utilizar medios gráficos para analizar la
función previamente.

En todos los casos indique el(los) valor(es) inicial(es) que utilizó y el número de
iteraciones que fueron necesarias para alcanzar la respuesta:
"""

import numpy as np
import sympy as sp
from sympy import symbols
from sympy.plotting import plot3d

x, y, z = symbols('x y z')


# -- ---------------------------------------------- FUNCION: Newton Raphson Multivariado -- #

def newton_raphson(param_sis, param_ini, param_error):
    """

    Parameters
    ----------
    param_sis : list : lista con objetos de funciones simbolicas
    param_ini : list : Lista con valores iniciales para variables
    param_error : float : 10e-3

    Returns
    ------
    valor_5

    Debugging
    ---------
    param_ini = [4, 2, -3]
    param_sis = [c1_f, c1_g, c1_h]
    param_error = 10e-3

    """

    # acomodar los parametros iniciales verticalmente
    np_param_ini = np.vstack(np.array(param_ini))
    # representar al sistema de ecuaciones en una matriz simbolica
    sistema = sp.Matrix(param_sis)
    # calcular la matriz jacobiana del sistema para solucionar una ecuacion tipo Ax=b
    jacobian = sistema.jacobian(variables)
    # calcular la inversa de la jacobiana
    jacobian_inv = jacobian.inv()
    # multiplicar
    mult = jacobian_inv * sistema
    # Error inicial
    error = float("inf")
    # contador de iteraciones
    iteraciones = 0
    sumadores = np_param_ini

    # hacer ciclo hasta sobrepasar medida de error
    while abs(error) > param_error:
        # contar iteraciones hechas
        iteraciones += 1
        # sustituir en ecuacion x = 1/A * B
        valores = -mult.subs(list(zip(variables, sumadores))) + sumadores
        # guardar valores encontrados provisionales
        sumadores = valores
        # calcular medida de error
        error = np.sum(mult.subs(list(zip(variables, valores))))

    # redondear a 4 de precision
    valores = [round(sumadores[i], 4) for i in range(0, len(sumadores))]

    return {'parametros': param_ini, 'solucion': valores, 'iteraciones': iteraciones}


# -- ------------------------------------------------------------------- Caso 2 variables -- #

# Sistema de ecuaciones
c1_f = 'x**2 + y - 1'
c1_g = 'x - 2*y**2'

# Sistema de ecuaciones
c2_f = 'x**2 - 10*x + y**2 + 5'
c2_g = 'x*y**2 + x - 10*y + 8'

# variables simbolicas
variables = [x, y]

# plots expandido para vision general
plot3d(c1_f, c1_g)

# Buscar solucion al sistema
ejercicio = newton_raphson(param_sis=[c2_f, c2_g],
                             param_ini=[10, 10],
                             param_error=10e-3)

# Parametros:
print('Parametros Iniciales: ', ejercicio['parametros'])
# Solucion:
print('Solucion: ', ejercicio['solucion'])
# Itearciones:
print('Iteraciones: ', ejercicio['iteraciones'])

# Comprobacion
solucion = np.vstack(np.array(ejercicio['solucion']))
sistema = sp.Matrix([c2_f, c2_g])
res = sistema.subs(list(zip(variables, solucion)))
print('comprobacion:\n', np.array(res))

# -- ----------------------------------------------------------------------- EJERCICIO 1 -- #
# c1_f = 'x**2 + y - 1'
# c1_g = 'x - 2*y**2'

# -- [7.5, -7.5]
# Parametros Iniciales:  [7.5, -7.5]
# Solucion:  [1.3524, -0.8262]
# Iteraciones:  5
# comprobacion:
#  [[0.00278289692141698]
#  [-0.0128209609538317]]

# -- [0, 0]
# Parametros Iniciales:  [0, 0]
# Solucion:  [0.6552, 0.5738]
# Iteraciones:  5
# comprobacion:
#  [[0.00308243022300303]
#  [-0.00329374719876796]]

# -- ----------------------------------------------------------------------- EJERCICIO 2 -- #
# c2_f = 'x**2 - 10*x + y**2 + 5'
# c2_g = 'x*y**2 + x - 10*y + 8'

# -- [-7.5, 0]
# Parametros iniciales: [-7.5, 0]
# iteraciones:  4
# solucion:  [0.6221, 0.9141]
# comprobacion:
#  [[0.00158113479847088]
#  [0.000909367466521260]]

# -- [10, 10]
# Parametros Iniciales:  [10, 10]
# Solucion:  [2.0758, 3.3838]
# Iteraciones:  31
# comprobacion:
#  [[0.00104069258668460]
#  [0.00594772052233594]]


# -- ------------------------------------------------------------------- Caso 3 variables -- #
c3_f = 'x + y - z + 2'
c3_g = 'x**2 + y'
c3_h = 'z - y**2 - 1'
variables = [x, y, z]

# Buscar solucion al sistema
ejercicio_3 = newton_raphson(param_sis=[c3_f, c3_g, c3_h],
                             param_ini=[1, -1, 0],
                             param_error=10e-3)

# Parametros:
print('Parametros Iniciales: ', ejercicio_3['parametros'])

# Solucion:
print('solucion: ', ejercicio_3['solucion'])

# Itearciones:
print('iteraciones: ', ejercicio_3['iteraciones'])

# Comprobacion
solucion = np.vstack(np.array(ejercicio_3['solucion']))
sistema = sp.Matrix([c3_f, c3_g, c3_h])
res = sistema.subs(list(zip(variables, solucion)))
print('comprobacion:\n', np.array(res))

# -- [-1, -1, 2]
# Parametros Iniciales:  [-1, -1, 2]
# solucion:  [-0.5699, -0.3247, 1.1054]
# iteraciones:  3
# comprobacion:
#  [[0]
#  [8.71925149112940e-5]
#  [-2.96161160804331e-5]]

# -- [1, -1, 0]
# Parametros Iniciales:  [1, -1, 0]
# solucion:  [1, -1, 2.00000000000000]
# iteraciones:  1
# comprobacion:
#  [[0]
#  [0]
#  [0]]
