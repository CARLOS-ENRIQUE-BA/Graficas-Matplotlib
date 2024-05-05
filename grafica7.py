import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(0.5 * x)

x = np.linspace(-10, 10, 400)
y = f(x)

plt.figure(figsize=(10, 5)) 

plt.plot(x, y, label='$f(x) = \cos\\left(\\frac{1}{2}x\\right)$', color='b')
plt.title('Gráfica de $f(x) = \cos\\left(\\frac{1}{2}x\\right)$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)
plt.legend()
plt.show()
