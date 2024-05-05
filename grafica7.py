import numpy as np
import matplotlib.pyplot as plt

def f_half(x):
    return np.cos(0.5 * x)

def f(x):
    return np.cos(x)

def f_double(x):
    return np.cos(2 * x)

x = np.linspace(-10, 10, 400)
y_half = f_half(x)
y = f(x)
y_double = f_double(x)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(x, y_half, label='$f(x) = \cos\\left(\\frac{1}{2}x\\right)$', color='b')
plt.title('Gráfica de $f(x) = \cos\\left(\\frac{1}{2}x\\right)$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(x, y, label='$f(x) = \cos(x)$', color='r')
plt.title('Gráfica de $f(x) = \cos(x)$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(x, y_double, label='$f(x) = \cos(2x)$', color='g')
plt.title('Gráfica de $f(x) = \cos(2x)$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
