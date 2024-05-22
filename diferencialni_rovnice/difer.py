import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def lorenz_atraktor(t, stav, sigma=10, rho=28, beta=8/3,):
    x, y, z = stav
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

def vyres_lorenzuv_atraktor(pocatecni_stav=[0, 1, 1.05], t_span=(0, 100), pocet_bodu=10000):
    t_eval = np.linspace(*t_span, pocet_bodu)
    reseni = solve_ivp(lorenz_atraktor, t_span, pocatecni_stav, t_eval=t_eval)
    return reseni

def vykresli_lorenzuv_atraktor(reseni):
    fig = plt.figure(figsize=(10, 8))
    sub_plot = fig.add_subplot(111, projection='3d')
    sub_plot.plot(reseni.y[0], reseni.y[1], reseni.y[2], label='Lorenzův atraktor')
    sub_plot.set_xlabel('X')
    sub_plot.set_ylabel('Y')
    sub_plot.set_zlabel('Z')
    sub_plot.set_title('Lorenzův atraktor')
    plt.legend()
    plt.show()

vykresli_lorenzuv_atraktor(vyres_lorenzuv_atraktor())
