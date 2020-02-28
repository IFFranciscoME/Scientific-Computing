
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II
# -- codigo: IDI_II_Tarea4_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import sympy as sy
from sympy.plotting import plot3d
from sympy import symbols, N

x, y, z = symbols('x y z')

f_1 = 'x**4 - 3*x**3 + 2'
# plot3d((f_1, (x, -5, 5), (y, -5, 5)))

f_2 = 'x**2 - 24*y + y**2 -10*y'
# plot3d((f_2, (x, -5, 5), (y, -5, 5)))

f_3 = sy.sin((1/2)*x**2 - (1/4)*y**2 + 3)*sy.cos(2*x + 1 - sy.exp(y))
# plot3d((f_3, (x, -5, 5), (y, -5, 5)))


# -- ---------------------------------------- FUNCION: Gradiente Descendente (Ascendente) -- #
# -- ------------------------------------------------------------------------------------ -- #
# -- --

def f_grad(param_fun, param_x0, param_y0, param_e, param_p):
    """
    Parameters
    ----------
    param_fun : str : funcion a utilizar
    param_x0 : numeric : valor inicial para x0
    param_y0 : numeric : valor inicial para y0
    param_e : numeric : exactitud deseada
    param_p : int : cantidad de digitos para la precision

    Returns
    -------
    p_x0 : numeric : componente en x del punto minimo (maximo) encontrado
    p_y0 : numeric : componente en y del punto minimo (maximo) encontrado

    Debugging
    ---------
    param_fun = 'x + y**2'
    param_x0 = 0
    param_y0 = 0
    param_e = 10e-3
    param_p = 4

    """

    # diferencial de la funcion respecto a x
    f_x = param_fun.diff(x)
    # diferencial de la funcion respecto a y
    f_y = param_fun.diff(y)
    # factor de "incremento"
    theta = .1

    # gradiente de la funcion
    gradiente = [f_x, f_y]

    x_n = param_x0 - theta*N(f_x.subs(x, param_x0).subs(y, param_y0)).evalf()
    y_n = param_y0 - theta*N(f_y.subs(y, param_y0).subs(x, param_x0)).evalf()

    return x_n, y_n
