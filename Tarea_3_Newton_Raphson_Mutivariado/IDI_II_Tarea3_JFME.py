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

import sympy as sp

# declarar a x, y, z como variables simbolicas
x, y, z = sp.symbols('x y z')

# -- ----------------------------------------------------------------------------- Caso 1 -- #
c1_f = 'x**2 + y - 1'
c1_g = 'x - 2*y**2'
X = sp.MatrixSymbol('A', 2, 1)

# -- ----------------------------------------------------------------------------- Caso 2 -- #
c2_f = 'x**2 - 10*x + y**2 + 5'
c2_g = 'x*y**2 + x - 10*y + 8'
c2_A = sp.MatrixSymbol('A', 2, 1)

# -- ----------------------------------------------------------------------------- Caso 3 -- #
c3_f = 'x + y - z + 2'
c3_g = 'x**2 + y'
c3_h = 'z - y**2 - 1'
c3_A = sp.MatrixSymbol('A', 3, 1)

