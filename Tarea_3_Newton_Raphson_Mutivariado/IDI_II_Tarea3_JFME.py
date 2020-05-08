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


class NewtonRaphson:
    """
    Metodo de Newton-Raphson Multivariado
    """
    def __init__(self, funciones, variables):
        # atributo de clase seran sus funciones
        self.funciones = funciones
        # guardar funciones en matriz para representarlas como sistema de ecuaciones
        matriz_sistema = sp.Matrix(funciones)
        # calcular la matriz jacobiana del sistema de funciones
        self.jacobiana = matriz_sistema.jacobian(variables)
        # obtener la inversa de la matriz jacobiana
        self.jacobiana_inv = self.jacobiana.inv()
        # operacion de multiplicacion de inversa de jacobiana por matriz del sistema
        self.mult = self.jacobiana_inv * matriz_sistema

    def metodo(self, valores_iniciales, variables, matrix_symbol, error):
        """
        Parameters
        ----------
        valores_iniciales
        variables
        matrix_symbol
        error
        """

        # valores iniciales
        valores_iniciales = sp.Matrix(valores_iniciales)

        for _ in range(15):
            valores = {}
            for i in range(len(valores_iniciales)):
                valores[variables[i]] = valores_iniciales[i]
            x_subs = self.mult.subs(zip(variables, valores_iniciales))


# funciones
# instanciar clase con sus parametros de inicializacion
funciones = [c1_f, c1_g]
variables = [x, y]
valores_iniciales = [2, 0.5]
ejercicio_1 = NewtonRaphson([c1_f, c1_g], [x, y])
