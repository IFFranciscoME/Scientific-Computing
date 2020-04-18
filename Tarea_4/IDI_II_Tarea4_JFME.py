
# -- ------------------------------------------------------------------------------------ -- #
# -- proyecto: IDI-II
# -- codigo: IDI_II_Tarea4_JFME.py
# -- repositorio: https://github.com/IFFranciscoME/IDI_II_GIT
# -- ------------------------------------------------------------------------------------ -- #

import sympy as sp
from sympy import symbols, N
from sympy.plotting import plot3d, plot


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


# Declarar x, y, z como variables simbolicas
x, y, z = symbols('x y z')

# Funcion 1
f_1 = 'x**4 - 3*x**3 + 2'
# Establecer que es una expresion con variable simbolica
f_n = sp.S(f_1)
# Graficar la funcion para explorar dominio
plot(f_1, (x, -2, +4))
# Evaluar funcion de gradiente descendente
f_grad(param_fun=0, param_x=0, param_y=0, param_e=0, param_p=0)

# -- Notas de ejercicio 1
# grafique de -10 a 10
# la funcion crece indefinidamente en ambos sentidos, hacia x++ y x--
# grafique, puse x0=-2, con theta = 0.5, resultado fue que mando a x=32

# Funcion 2
f_2 = 'x**2 - 24*y + y**2 -10*y'
# Establecer que es una expresion con variable simbolica
f_2 = sp.S(f_2)
# Graficar la funcion para explorar dominio
plot3d(f_2, (x, -4, +4), (y, -4, +4))
# Evaluar funcion de gradiente descendente
f_grad(param_fun=f_2, param_x=1, param_y=-3, param_e=10e-3, param_p=4)

# -- Notas de ejercicio 2
# grafique de x=-10 a x=10, y=-10 a y=10 y note que la funcion es bastante "simple"
# reduje a -4 todos los valores
# deje a x=1 y y =-3 y fue bastante rapida la convergencia

# Funcion 3
f_3 = 'sin((1/2)*x**2 - (1/4)*y**2 + 3)*cos(2*x + 1 - exp(y))'
# Establecer que es una expresion con variable simbolica
f_3 = sp.S(f_3)
# Graficar la funcion para explorar dominio
plot3d(f_3, (x, -4, +4), (y, -4, +4))
# Evaluar funcion de gradiente descendente
f_grad(param_fun=f_3, param_x=-1, param_y=-4, param_e=10e-3, param_p=4)

# -- Notas de ejercicio 3
# grafique de x=-4 a x=4, y=-4 a y=4 y note que la funcion es bastante "complicada"
# deje valores de x=-1 a y=-4, que elegi visualmente como una "cima" o valor maximo
# y la funcion convergio bastante rapido a un minimo local
