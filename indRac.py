from sympy import symbols, Limit, simplify

# Definimos la variable simbólica x
x = symbols('x')

# Definimos la función cuyo límite queremos calcular
f = (x**2 - 4)/(x - 2)

# Calculamos el límite indeterminado de f(x) cuando x tiende a 2 por racionalización
limite = Limit(simplify(f).subs(x, 2 + h) - simplify(f).subs(x, 2), h, 0)

# Imprimimos el resultado del límite
print(limite.doit())
