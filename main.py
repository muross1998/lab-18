import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import fsolve

X = np.linspace(-5, 3, 100) 
Y = X**2 + 4*X 
plt.plot(X, Y, 'k-', label='Функція $y = x^2 + 4x$')


Y1 = np.gradient(Y, X[1] - X[0])
plt.plot(X, Y1, 'k--', label="Похідна $dy/dx$")


Y_int = cumulative_trapezoid(Y, X, initial=0)
plt.plot(X, Y_int, 'k:', label='Первісна $Y$')


Y_line = X
plt.plot(X, Y_line, color='gray', linestyle='-.', label='Пряма $y = x$')


def intersection_eq(x):
    return (x**2 + 4*x) - x

roots = fsolve(intersection_eq, [-3, 0])

for root in roots:
    plt.plot(root, root, 'ro') 
    plt.text(root + 0.2, root - 1, f'({root:.0f}; {root:.0f})', color='red', weight='bold')

plt.xlabel('$x$')
plt.ylabel('$y, \\dot{y}, Y$')
plt.grid(True)

plt.legend()

plt.show()
