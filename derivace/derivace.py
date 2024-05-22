import numpy as np
import sympy as sp

def funkce(x):
    return 1 / (x**2 + x)

def derivace_adaptabilni_krok(funkce, x, epsilon, h=1e-5):
    h = np.sqrt(epsilon) * (1 + np.abs(x))
    dy_dx = (funkce(x + h) - funkce(x - h)) / (2 * h)
    return dy_dx

def derivace_pevny_krok(funkce, x, h=1e-5):
    dy_dx = (funkce(x + h) - funkce(x - h)) / (2 * h)
    return dy_dx

def derivace_analyticky(x_value):
    x = sp.symbols('x')
    return sp.diff(funkce(x), x).subs(x, x_value)

x = np.pi / 2
epsilon = 1e-8


print(f"Numerická derivace s adaptabilním krokem: {derivace_adaptabilni_krok(funkce, x, epsilon)}")
print(f"Numerická derivace s pevným krokem: {derivace_pevny_krok(funkce, x)}") 
print(f"Analytická derivace: {derivace_analyticky(x)}")
