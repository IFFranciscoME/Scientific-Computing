
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II
# -- codigo: IDI_II_Tarea4_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import sympy as sy
from sympy.plotting import plot3d
from sympy import symbols

x, y, z = symbols('x y z')

f_1 = 'x**4 - 3*x**3 + 2'
plot3d((f_1, (x, -5, 5), (y, -5, 5)))

f_2 = 'x**2 - 24*y + y**2 -10*y'
plot3d((f_2, (x, -5, 5), (y, -5, 5)))

f_3 = sy.sin((1/2)*x**2 - (1/4)*y**2 + 3)*sy.cos(2*x + 1 - sy.exp(y))
plot3d((f_3, (x, -5, 5), (y, -5, 5)))
