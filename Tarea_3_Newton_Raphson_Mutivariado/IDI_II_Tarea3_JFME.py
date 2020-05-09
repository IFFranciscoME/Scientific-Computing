
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

    np_param_ini = np.vstack(np.array(param_ini))
    sistema = sp.Matrix(param_sis)
    jacobian = sistema.jacobian(variables)
    jacobian_inv = jacobian.inv()
    mult = jacobian_inv * sistema

    error = float("inf")
    iteraciones = 0
    sumadores = np_param_ini

    # valores = -mult.subs(list(zip(variables, param_ini))) + np_param_ini
    # error = np.sum(-mult.subs(list(zip(variables, param_ini))))
    # print('error previo', error)

    while abs(error) > param_error:

        iteraciones += 1
        valores = -mult.subs(list(zip(variables, sumadores))) + sumadores
        sumadores = valores
        error = np.sum(mult.subs(list(zip(variables, valores))))

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
                             param_ini=[15, -15],
                             param_error=10e-3)

# Parametros:
print('Parametros Iniciales: ', ejercicio['parametros'])
# Solucion:
print('Solucion: ', ejercicio['solucion'])
# Itearciones:
print('Iteraciones: ', ejercicio['iteraciones'])

# Comprobacion
solucion = np.vstack(np.array(ejercicio['solucion']))
sistema = sp.Matrix([c1_f, c1_g])
res = sistema.subs(list(zip(variables, solucion)))
print('comprobacion:\n', np.array(res))

# plot focalizado a resultados
plot3d(c1_f, c1_g,
       (x, solucion[0][0]*.90, solucion[0][0]*1.10),
       (y, solucion[1][0]*.90, solucion[1][0]*1.10))


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

# -- ----------------------------------------------------------------------------- Caso 3 -- #
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

# -- ----------------------------------------------------------------------- Caso Ejemplo -- #

# c1_f = 'x**3 + y**3 - z**3 - 129'
# c1_g = 'x**2 + y**2 - z**2 - 9.75'
# c1_h = 'x + y - z - 9.49'
#
# # [4.3621, 1.6619, -3.4660]
#
# variables = [x, y, z]
#
# ejercicio_1 = newton_raphson(param_sis=[c1_f, c1_g, c1_h],
#                              param_ini=[4, 2, -3],
#                              param_error=10e-3)
# print(ejercicio_1)
