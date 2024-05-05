import numpy as np
import matplotlib.pyplot as plt

def F(x):
    return np.abs(x - 2) + 3

x = np.linspace(-10, 10, 400)
y = F(x)

plt.plot(x, y, label='$F(x) = |x - 2| + 3$', color='b')
plt.title('Gráfica de $F(x) = |x - 2| + 3$')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.grid(True)
plt.legend()
plt.show()
