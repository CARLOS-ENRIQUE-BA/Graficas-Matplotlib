import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)
x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = f(x)

plt.plot(x, y, label='$f(x) = \sin(x)$', color='b')
plt.title('Gráfica de $f(x) = \sin(x)$')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 
plt.gca().spines['left'].set_position('center')
plt.gca().spines['bottom'].set_position('center')
plt.grid(True)
plt.show()
