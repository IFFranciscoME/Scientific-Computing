
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II
# -- codigo: IDI_II_Tarea3_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import time
import sympy as sp
from sympy.plotting import plot3d
from sympy import symbols

# -- NOTAS
# -- -- Utilizar la inversa de sympy

# -- Caso 1
# -- -- f(x,y) = x**2 + y - 1
# -- -- g(x,y) = x - 2*y**2

x, y, z = symbols('x y z')
c1_f = 'x**2 + y - 1'
c1_g = 'x - 2*y**2'

plot3d((c1_f, (x, -5, 5), (y, -5, 5)),
       (c1_g, (x, -5, 5), (y, -5, 5)))

# -- Caso 2
# -- -- f(x,y) = x**2 - 10*x + y**2 + 5
# -- -- g(x,y) = x*y**2 + x - 10*y + 8

c2_f = 'x**2 - 10*x + y**2 + 5'
c2_g = 'x*y**2 + x - 10*y + 8'

plot3d((c2_f, (x, -5, 5), (y, -5, 5)),
       (c2_g, (x, -5, 5), (y, -5, 5)))

# -- Caso 3
# -- -- f(x,y) = x + y - z + 2
# -- -- g(x,y) = x**2 + y
# -- -- h(x,y) = z - y**2 - 1

c3_f = 'x + y - z + 2'
c3_g = 'x**2 + y'
c3_h = 'z - y**2 - 1'

plot3d((c3_f, (x, -5, 5), (y, -5, 5), (z, -5, 5)),
       (c3_g, (x, -5, 5), (y, -5, 5), (z, -5, 5)),
       (c3_h, (x, -5, 5), (y, -5, 5), (z, -5, 5)))

# -- Paso 1
