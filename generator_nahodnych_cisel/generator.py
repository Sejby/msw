import random as r
import pyautogui
import numpy as np

def ziskej_seminko_z_pozice_mysi():
    x, y = pyautogui.position()
    seed = np.sqrt(x * y / y * 100000)
    return seed

def nahodne_cislo(seed):
    r.seed(seed)
    print(f"náhodné číslo: {r.randint(0,10)}")    


nahodne_cislo(ziskej_seminko_z_pozice_mysi())

