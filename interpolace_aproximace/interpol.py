import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, UnivariateSpline

# Definice funkcí
def harmonicka_funkce(x):
    return np.sin(x)

def logaritmicka_funkce(x):
    return np.log(x)

def kvadraticka_funkce(x):
    return x**2

# Funkce pro výpočet přesnosti
def vypocitej_presnost(skutecne_hodnoty, interpolovane_hodnoty):
    rozdily = skutecne_hodnoty - interpolovane_hodnoty
    mse = np.mean(rozdily ** 2)
    return mse

# Funkce pro interpolaci
def interpolace_funkce(x, y, metoda):
    if metoda == 'linear' or metoda == 'cubic':
        return interp1d(x, y, kind=metoda)
    elif metoda == 'quadratic':
        return UnivariateSpline(x, y, k=2, s=0)

# Generování dat a interpolace
def vypocitej(nazev_funkce, funkce, metoda):
    x = np.linspace(1, 10, 100)
    y = funkce(x) + np.random.normal(0, 0.1, len(x))

    # Náhodný výběr bodů
    indexy = np.random.choice(len(x), size=20, replace=False)
    vzorky_x = x[indexy]
    vzorky_y = y[indexy]
    
    # Interpolace
    interp = interpolace_funkce(vzorky_x, vzorky_y, metoda)
    jemna_osa_x = np.linspace(1, 10, 1000)
    interp_osa_y = interp(jemna_osa_x)
    
    return jemna_osa_x, interp_osa_y, funkce(jemna_osa_x), vzorky_x, vzorky_y

# Vykreslení grafu
def vykresli_graf(nazev_funkce, jemna_osa_x, skutecne_hodnoty, interp_osa_y, vzorky_x, vzorky_y, metoda):
    plt.plot(jemna_osa_x, skutecne_hodnoty, label='Původní funkce')
    plt.scatter(vzorky_x, vzorky_y, label='Vzorky s šumem', color='black')
    plt.plot(jemna_osa_x, interp_osa_y, label=f'Interpolace - {metoda}', color='red')
    plt.xlabel('osa x')
    plt.ylabel('osa y')
    plt.title(f'Interpolace a aproximace funkce: {nazev_funkce}')
    plt.legend()
    plt.show()

# Výpočet a vykreslení pro všechny funkce a metody
funkce_list = [('Harmonická funkce', harmonicka_funkce), ('Logaritmická funkce', logaritmicka_funkce), ('Kvadratická funkce', kvadraticka_funkce)]
metody = ['linear', 'cubic', 'quadratic']

for nazev_funkce, funkce in funkce_list:
    for metoda in metody:
        jemna_osa_x, interp_osa_y, skutecne_hodnoty, vzorky_x, vzorky_y = vypocitej(nazev_funkce, funkce, metoda)
        vykresli_graf(nazev_funkce, jemna_osa_x, skutecne_hodnoty, interp_osa_y, vzorky_x, vzorky_y, metoda)
        mse = vypocitej_presnost(skutecne_hodnoty, interp_osa_y)
        print(f"{nazev_funkce}, metoda {metoda}: Součet čtverců rozdílů = {mse}")
