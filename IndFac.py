from sympy import symbols, Limit, factor

# Definimos la variable simbólica x
x = symbols('x')

# Definimos la función cuyo límite queremos calcular
f = x**2 - 4*x + 3

# Calculamos el límite indeterminado de f(x) cuando x tiende a 1 por factorización
limite = Limit(factor(f), x, 1)

# Imprimimos el resultado del límite
print(limite.doit())
