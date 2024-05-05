import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.abs(1 - x**2) + 3

x = np.linspace(-2, 2, 400)
y = f(x)

plt.plot(x, y, color='r', label='$|1 - x^2| + 3$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de $|1 - x^2| + 3$')
plt.legend()
plt.grid(True)
plt.show()

