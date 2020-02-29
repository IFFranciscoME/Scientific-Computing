
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II
# -- codigo: IDI_II_Tarea4_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import sympy as sp
from sympy import symbols, N
# from sympy.plotting import plot3d, plot

# Declarar x, y, z como variables simbolicas
x, y, z = symbols('x y z')
# Declarar funcion
f_1 = 'x**4 - 3*x**3 + 2'
f_2 = 'x**2 - 24*y + y**2 -10*y'
f_3 = 'sy.sin((1/2)*x**2 - (1/4)*y**2 + 3)*sy.cos(2*x + 1 - sy.exp(y))'

# Establecer que es una expresion con variable simbolica
# f_n = sp.S(f_1)
# Graficar la funcion para explorar dominio
# plot(f_1, (x, -4, +4))
# Derivada parcial de funcion respecto a x
# f_n.diff(x)


# -- ---------------------------------------- FUNCION: Gradiente Descendente (Ascendente) -- #
# -- ------------------------------------------------------------------------------------ -- #
# -- --

def f_grad(param_fun, param_x, param_y, param_e, param_p):
    """
    Parameters
    ----------
    param_fun : str : funcion a utilizar
    param_x : numeric : valor inicial para x0
    param_y : numeric : valor inicial para y0
    param_e : numeric : exactitud deseada
    param_p : int : cantidad de digitos para la precision

    Returns
    -------
    p_x0 : numeric : componente en x del punto minimo (maximo) encontrado
    p_y0 : numeric : componente en y del punto minimo (maximo) encontrado

    Debugging
    ---------
    param_fun = 'x**2 - 24*y + y**2 -10*y'
    param_x = -2
    param_y = 0
    param_e = 10e-3
    param_p = 4
    """

    # Establecer que es una expresion con variable simbolica
    param_fun = sp.S(param_fun)
    # diferencial de la funcion respecto a x
    f_x = param_fun.diff(x)
    # diferencial de la funcion respecto a y
    f_y = param_fun.diff(y)
    # factor de "incremento"
    theta = .1
    # iteraciones
    iteraciones = 0

    while True:
        # evaluacion de expresion de gradiente descendente

        temp_x = theta*N(f_x.subs(x, param_x).subs(y, param_y)).evalf()
        temp_y = theta*N(f_y.subs(x, param_x).subs(y, param_y)).evalf()

        # actualizar contador de iteraciones
        iteraciones += 1
        print(iteraciones)

        if abs(temp_x - param_x) < param_e and abs(temp_y - param_y) < param_e:
            break

        if iteraciones > 100:
            print("Algo paso que son muchas iteraciones sin llegar al resultado")
            break

        param_x = temp_x
        param_y = temp_y

    print("f(x,y) = " + str(param_fun) + "converge")
    print("el número de interaciones fueron: ", iteraciones, sep=" ")
    print('el error es: ' + str(abs(temp_x - param_x)))

# grafique, puse x0=-2, con theta = 0.5, resultado fue que mando a x=32

