import numpy as np
import matplotlib.pyplot as plt

def f_sin(x):
    return np.sin(x)

def f_abs_sin(x):
    return np.abs(np.sin(x))

x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_sin = f_sin(x)
y_abs_sin = f_abs_sin(x)

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(x, y_sin, label='$f(x) = \sin(x)$', color='b')
plt.title('Gráfica de $f(x) = \sin(x)$')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, y_abs_sin, label='$f(x) = | \sin(x) |$', color='r')
plt.title('Gráfica de $f(x) = | \sin(x) |$')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)

plt.tight_layout()
plt.show()
