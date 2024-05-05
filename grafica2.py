import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def f_up(x):
    return x**2 + 2

def f_down(x):
    return x**2 - 2

x = np.linspace(-3, 3, 400)

y = f(x)
y_up = f_up(x)
y_down = f_down(x)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y_up, color='r', label='$f(x) = x^2 + 2$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 
plt.title('Gráfica de $f(x) = x^2 + 2$')
plt.legend()
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position(('data', 0)) 
plt.xticks([-3, -2, -1, 1, 2, 3])
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(x, y, color='g', label='$f(x) = x^2$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 
plt.title('Gráfica de $f(x) = x^2$')
plt.legend()
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position(('data', 0)) 
plt.xticks([-3, -2, -1, 1, 2, 3]) 
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(x, y_down, color='b', label='$f(x) = x^2 - 2$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.title('Gráfica de $f(x) = x^2 - 2$')
plt.legend()
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position(('data', 0)) 
plt.xticks([-3, -2, -1, 1, 2, 3])
plt.grid(True)

plt.tight_layout()
plt.show()
