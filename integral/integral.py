import numpy as np
import sympy as sp

x = sp.Symbol('x')

parabola = x**2 + 2*x + 3
tangens = sp.tan(x)
logaritmus = sp.log(x + 2)

vysledek1 = sp.integrate(parabola, (x, 0, 5))
vysledek2 = sp.integrate(tangens, (x, 0, 1))
vysledek3 = sp.integrate(logaritmus, (x, 0, 5))

print(f"Výsledek f(x) = {parabola}, od 0 do 5: {vysledek1}")
print(f"Výsledek f(x) = {tangens} od 0 do 1: {vysledek2}")
print(f"Výsledek f(x) = {logaritmus} od 0 do 5: {vysledek3}")
