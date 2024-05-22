import time
import numpy as np
import sympy as sp
import math

def prvocisla_porovnani():
    def je_prvocislo(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    start_time = time.time()
    prvocisla_standard = []
    for i in range(2, 1000):
        if je_prvocislo(i):
            prvocisla_standard.append(i)
    end_time = time.time()
    standardni_cas = end_time - start_time

    start_time = time.time()
    prvocisla_numpy = []
    for i in range(2, 1000):
        if np.all(np.arange(2, np.sqrt(i) + 1) % i):
            prvocisla_numpy.append(i)
    prvocisla_numpy = np.array(prvocisla_numpy)
    end_time = time.time()
    numpy_cas = end_time - start_time

    return prvocisla_standard, standardni_cas, prvocisla_numpy, numpy_cas

def fibonacci_porovnani():
    def fibonacci_rekurzivni(n):
        if n <= 1:
            return n
        else:
            return fibonacci_rekurzivni(n-1) + fibonacci_rekurzivni(n-2)

    start_time = time.time()
    fibonacci_rekurzivni_vysledek = fibonacci_rekurzivni(30)
    end_time = time.time()
    rekurzivni_cas = end_time - start_time

    def fibonacci_iterativni(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    start_time = time.time()
    fibonacci_iterativni_vysledek = fibonacci_iterativni(30)
    end_time = time.time()
    iterativni_cas = end_time - start_time

    start_time = time.time()
    fibonacci_numpy_vysledek = []
    for i in range(30):
        fibonacci_numpy_vysledek.append(fibonacci_rekurzivni(i))
    fibonacci_numpy_vysledek = np.array(fibonacci_numpy_vysledek)
    end_time = time.time()
    numpy_cas = end_time - start_time

    return fibonacci_rekurzivni_vysledek, rekurzivni_cas, fibonacci_iterativni_vysledek, iterativni_cas, fibonacci_numpy_vysledek[-1], numpy_cas

def odmocnina_porovnavani():
    
    start_time = time.time()
    odmocnina_sympy = sp.log(2**933 / 3.14541541817748751524121178 * (25684894 / 0.6549845616518948748794986))
    end_time = time.time()
    sympy_cas = end_time - start_time

    start_time = time.time()
    odmocnina_standard = math.log(2**933 / 3.14541541817748751524121178 * (25684894 / 0.6549845616518948748794986))
    end_time = time.time()
    standardni_cas = end_time - start_time

    return odmocnina_sympy, sympy_cas, odmocnina_standard, standardni_cas

def arcuscosinus_porovnavani():
    x = 0.5
    start_time = time.time()
    arccosinus_standard = math.acos(x)
    end_time = time.time()
    standardni_cas = end_time - start_time

    start_time = time.time()
    arccosinus_sympy = sp.acos(x)
    end_time = time.time()
    sympy_cas = end_time - start_time

    return arccosinus_standard, standardni_cas, arccosinus_sympy, sympy_cas


def vektorovy_soucet_porovnani():
    vektor_standard = list(range(1000000))
    start_time = time.time()
    soucet_standard = sum(vektor_standard)
    end_time = time.time()
    standardni_cas = end_time - start_time

    vektor_numpy = np.arange(1000000)
    start_time = time.time()
    soucet_numpy = np.sum(vektor_numpy)
    end_time = time.time()
    numpy_cas = end_time - start_time

    return soucet_standard, standardni_cas, soucet_numpy, numpy_cas

prvocisla_standard, standardni_cas, prvocisla_numpy, numpy_cas = prvocisla_porovnani()
print(f"Prvočísla pomocí standardního pythonu - čas: {standardni_cas}")
print(f"Prvočísla pomocí numpy - čas: {numpy_cas}")

fibonacci_rekurzivni_vysledek, rekurzivni_cas, fibonacci_iterativni_vysledek, iterativni_cas, fibonacci_numpy_vysledek, numpy_cas = fibonacci_porovnani()
print(f"Výsledek fibonacciho posloupnosti (rekurzivní): {fibonacci_rekurzivni_vysledek} - čas: {rekurzivni_cas}")
print(f"Výsledek fibonacciho posloupnosti (iterativní): {fibonacci_iterativni_vysledek} - čas:  {iterativni_cas}")
print(f"Výsledek fibonacciho posloupnosti (NumPy): {fibonacci_numpy_vysledek}- čas: {numpy_cas}")

derivace_sympy, sympy_cas, derivace_standard, standardni_cas = odmocnina_porovnavani()
print(f"Odmocnina pomocí sympy: {derivace_sympy} - čas: {sympy_cas}")
print(f"Odmocnina pomocí standartního pythonu: {derivace_standard} - čas: {standardni_cas}")

arccosinus_sympy, sympy_cas, arccosinus_standard, standardni_cas = arcuscosinus_porovnavani()
print(f"Arcuscosinus pomocí sympy: {arccosinus_sympy} - čas: {sympy_cas}")
print(f"Arcuscosinus pomocí standartního pythonu: {arccosinus_standard}- čas: {standardni_cas}")