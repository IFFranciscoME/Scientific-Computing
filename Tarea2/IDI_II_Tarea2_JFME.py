# -- ------------------------------------------------------------------------------------ -- #
# --
# --
# --
# -- ------------------------------------------------------------------------------------ -- #

import decimal
import time
import sympy as sp
from sympy.plotting import plot


# -- ------------------------------------------------------------ FUNCION: Newton-Raphson -- #
# -- ------------------------------------------------------------------------------------ -- #
# -- Metodo de newton-raphson con variable simbolica

def f_newton_raphson(param_f, param_x0, param_e, param_msn):
    """
    Parameters
    ----------
    param_f : str : funcion para aproximar escrita entre comillas como string.
    param_x0 : int / float : valor inicial para correr el metodo.
    param_e : notacion cientifica (10e-4) : cota de error a superar.
    param_msn : bool : True = imprimir mensajes de calculos

    Returns
    -------
    dict('iteraciones' = iteraciones, 'tiempo' = tiempo, 'error' = epsilon,
         'valor_aprox' = x0, 'grafica' = grafica)

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
            # Activar bandera de error para que pare ciclo e imprimir el error
            raise
        # Ultimo error calculado en metodo
        epsilon = abs((xn - x0) / xn)
        # Iteraciones que se llevan
        iteraciones += 1
        # Actualizar el valor
        x0 = xn
        # Si param_msn == True, imprimir valores
        if param_msn:
            print('iteracion: ' + str(iteraciones) + ' | ' + 'Valor Aprox: ' + str(float(x0)))

    # Tiempo total transcurrido utilizando la funcion
    tiempo = round(time.time() - inicia, 4)

    return {'iteraciones': iteraciones, 'tiempo': tiempo, 'error': float(epsilon),
            'valor_aprox': float(x0)}


# -- Plots
# x = sp.Symbol('x')
# sp.plotting.plot3d(f2, (x, 1.7, 1.75))

# -- Ejercicio 1
f1a = 'x**3 - 2*x**2 - 5'
f1b = 'x - cos(x)'
f1c = 'x - 0.8 - 0.2*sin(x)'
f1d = 'log(x - 1) + cos(x-1)'
f1e = 'exp(x) - 3*x**2'

# ejercicio_a = f_newton_raphson(param_f=f1a, param_x0=.1, param_e=10e-4, param_msn=True)
# print(ejercicio_a)

# ejercicio_b = f_newton_raphson(param_f=f1b, param_x0=.1, param_e=10e-4, param_msn=True)
# print(ejercicio_b)

# ejercicio_c = f_newton_raphson(param_f=f1c, param_x0=2, param_e=10e-4, param_msn=True)
# print(ejercicio_c)

# ejercicio_d = f_newton_raphson(param_f=f1d, param_x0=2.5, param_e=10e-4, param_msn=True)
# print(ejercicio_d)

# ejercicio_e = f_newton_raphson(param_f=f1e, param_x0=1, param_e=10e-4, param_msn=True)
# print(ejercicio_e)

# -- Ejercicio 2
f2 = 'x**(1/2)'
plot(f2)

# numero para encontrarle raiz
num = 3

# no parar hasta encontrar mas decimales que 1e-6
while str(num)[::-1].find('.') < 5:
    # formula simplificada de metodo
    num = (num + float(num) / num) / 2  # update
# imprimir numero
print(num)

# -- Ejercicio 3
f3 = 'ln(x**2 + 1) - E**(0.4*x)*cos(pi*x)'
plot(f3)

ejercicio_3 = f_newton_raphson(param_f=f3, param_x0=-0.43, param_e=10e-6, param_msn=True)
print(ejercicio_3)
print(float(ejercicio_3['error']))
