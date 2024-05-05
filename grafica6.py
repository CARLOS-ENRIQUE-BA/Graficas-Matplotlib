import numpy as np
import matplotlib.pyplot as plt

def f_cos(x):
    return np.cos(x)

def f_half_cos(x):
    return 0.5 * np.cos(x)

def f_double_cos(x):
    return 2 * np.cos(x)

x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

y_cos = f_cos(x)
y_half_cos = f_half_cos(x)
y_double_cos = f_double_cos(x)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y_half_cos, label='$f(x) = \\frac{1}{2} \cos(x)$', color='r')
plt.title('Gráfica de $f(x) = \\frac{1}{2} \cos(x)$')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(x, y_cos, label='$f(x) = \cos(x)$', color='b')
plt.title('Gráfica de $f(x) = \cos(x)$')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(x, y_double_cos, label='$f(x) = 2 \cos(x)$', color='g')
plt.title('Gráfica de $f(x) = 2 \cos(x)$')
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
