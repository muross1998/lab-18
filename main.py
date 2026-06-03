import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
from scipy.optimize import fsolve

def f(x, a):

    i = 9 
    return (i + x) / (-i + 2.5 * i + x) + np.sin(x + np.pi / 2)**(i + 1) + a

def f2(x):
    return x

dx = 0.1
X = np.arange(-1, 2.1, dx)

def update(c=(0, 1, 0.1), a=(-1, 1, 0.1)):
    plt.figure(figsize=(10, 6))
  
    Y = f(X, a) 

    Y_ = np.diff(Y) / np.diff(X) 

    Y_int = Y.cumsum() * dx + c 

    plt.plot(X, Y, label="Функція $f(x)$", linewidth=2)
    plt.plot(X[:-1] + dx/2, Y_, label="Похідна $f'(x)$")
    plt.plot(X, Y_int, label="Первісна $F(x)$")
    plt.plot(X, f2(X), "--", color="red", label="Пряма $y=x$")
    

    f3 = lambda x: f(x, a) - f2(x) 

    x0 = fsolve(f3, np.array([-1, 0, 1, 2]))
 
    x0_unique = np.unique(np.round(x0, 3))
    valid_roots = x0_unique[(x0_unique >= -1) & (x0_unique <= 2.1)]
    
    for root in valid_roots:
        y_val = f(root, a)
        plt.scatter(root, y_val, color='red', s=50, zorder=5)
        plt.annotate(f'({root:.2f}; {y_val:.2f})', 
                     (root, y_val), textcoords="offset points", 
                     xytext=(0,10), ha='center', weight='bold')


    plt.legend()
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title('Інтерактивний графік: Функція, Похідна, Первісна та Перетин')
    plt.show()

interact(update)
