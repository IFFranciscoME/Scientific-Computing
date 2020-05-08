
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
    param_error = 10e-2

    """

    np_param_ini = np.vstack(np.array(param_ini))
    sistema = sp.Matrix(param_sis)
    jacobian = sistema.jacobian(variables)
    jacobian_inv = jacobian.inv()
    mult = jacobian_inv * sistema

    error = float("inf")
    valores = -mult.subs(list(zip(variables, param_ini))) + np_param_ini
    error = np.sum(-mult.subs(list(zip(variables, param_ini))))

    iteraciones = 0

    while error > param_error:

        iteraciones += 1
        valores = -mult.subs(list(zip(variables, valores)))
        valores_n = valores + np_param_ini
        error = np.sum(valores)
        valores = valores_n

    valores = [round(valores[i], 4) for i in range(0, len(valores))]

    return {'solucion': valores, 'iteraciones': iteraciones}


# -- ----------------------------------------------------------------------------- Caso 1 -- #

# Sistema de ecuaciones
c1_f = 'x**2 + y - 1'
c1_g = 'x - 2*y**2'
variables = [x, y]

# plot expandido para vision general
plot3d(c1_f, c1_g)

# Buscar solucion al sistema
ejercicio_1 = newton_raphson(param_sis=[c1_f, c1_g],
                             param_ini=[0, 0],
                             param_error=1e-3)

# -- Resultados
# Valores Iniciales:
# [0, 0]

# Itearciones:
print(ejercicio_1['iteraciones'])

# Solucion:
print(ejercicio_1['solucion'])

# plot focalizado a resultados
plot3d(c1_f, c1_g, (x, -1, 0), (y, -3, -0.5))

# -- ----------------------------------------------------------------------------- Caso 2 -- #

# ecuaciones
c2_f = 'x**2 - 10*x + y**2 + 5'
c2_g = 'x*y**2 + x - 10*y + 8'

# plot expandido para vision general
plot3d(c2_f, c2_g)

# Buscar solucion al sistema
ejercicio_2 = newton_raphson(param_sis=[c2_f, c2_g],
                             param_ini=[0, 0],
                             param_error=1e-14)
# valores de variables
print(ejercicio_2)

# plot focalizado
plot3d(c1_f, c1_g, (x, -1, 0), (y, -3, -0.5))

# -- ----------------------------------------------------------------------------- Caso 3 -- #
# c3_f = 'x + y - z + 2'
# c3_g = 'x**2 + y'
# c3_h = 'z - y**2 - 1'

# -- ----------------------------------------------------------------------- Caso Ejemplo -- #

c1_f = 'x**3 + y**3 - z**3 - 129'
c1_g = 'x**2 + y**2 - z**2 - 9.75'
c1_h = 'x + y - z - 9.49'

variables = [x, y, z]

ejercicio_1 = newton_raphson(param_sis=[c1_f, c1_g, c1_h],
                             param_ini=[4, 2, -3],
                             param_error=1e-14)
print(ejercicio_1)
