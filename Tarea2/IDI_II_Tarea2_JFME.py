
# -- ------------------------------------------------------------------------------------ -- #
# --
# --
# --
# -- ------------------------------------------------------------------------------------ -- #

import time
import sympy as sp
from sympy.plotting import plot


# -- ------------------------------------------------------------ FUNCION: Newton-Raphson -- #
# -- ------------------------------------------------------------------------------------ -- #
# -- Metodo de newton-raphson con variable simbolica

def f_newton_raphson(param_f, param_x0, param_e):
    """
    Parameters
    ----------
    param_f :
    param_x0 :
    param_e :

    Returns
    -------
    val =

    Debugging
    ---------
    # Funcion para aproximar
    param_f = 'x ** 3 - 2 * x ** 2 - 5'
    # Valor inicial
    param_x0 = 1.0
    # Cota de error
    param_e = 10e-4

    """
    # Declarar cual sera la variable simbolica
    x = sp.Symbol('x')
    # Declarar la expresion
    param_f = sp.S(param_f)

    # Inicializar epislon en error
    epsilon = 1
    # Para calculo de tiempo de ejecucion
    inicia = time.time()
    # Para guardar cantidad de interaciones realizadas
    iteraciones = 0
    # inicializar parametro
    x0 = param_x0

    # Calcular mientras el error obtenido sea mayor al error objetivo
    while epsilon > param_e:
        # Intentar hacer division para "cachar" un error de division entre 0
        try:
            xn = x0 - param_f.subs(x, x0) / sp.diff(param_f, x).subs(x, x0)
        # Rompe el ciclo si "cacha" el error de division entre 0
        except ZeroDivisionError:
            print("La derivada de la funcion evaluada en x0 dio 0.")
            # Activar bandera de error para que pare ciclo
            raise
        # Ultimo error calculado en metodo
        epsilon = abs((xn - x0) / xn)
        # Iteraciones que se llevan
        iteraciones += 1
        # Actualizar el valor
        x0 = xn

    # Tiempo total transcurrido utilizando la funcion
    tiempo = round(time.time() - inicia, 4)

    # Grafica
    grafica = param_f

    return {'iteraciones': iteraciones, 'tiempo': tiempo, 'error': epsilon,
            'valor_aprox': x0, 'grafica': grafica}


fa = 'x**3 - 2*x**2 - 5'
fb = 'x - cos(x)'
fc = 'x - 0.8 - 0.2*sin(x)'
fd = 'log(x - 1) + cos(x-1)'
fe = 'e**x - 3*x**2'

ejercicio_a = f_newton_raphson(param_f=fc, param_x0=.1, param_e=10e-4)
print(ejercicio_a)

ejercicio_b = f_newton_raphson(param_f=fb, param_x0=.1, param_e=10e-4)
print(ejercicio_b)

ejercicio_c = f_newton_raphson(param_f=fc, param_x0=.1, param_e=10e-4)
print(ejercicio_c)

ejercicio_d = f_newton_raphson(param_f=fd, param_x0=.1, param_e=10e-4)
print(ejercicio_d)

ejercicio_e = f_newton_raphson(param_f=fe, param_x0=.1, param_e=10e-4)
print(ejercicio_e)
