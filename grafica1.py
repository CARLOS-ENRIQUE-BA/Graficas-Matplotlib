import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def f_left(x):
    return (x + 2)**2

def f_right(x):
    return (x - 2)**2

x = np.linspace(-5, 5, 400)

y = f(x)
y_left = f_left(x)
y_right = f_right(x)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y_left, color='r', label='$f(x) = (x + 2)^2$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 
plt.xlabel('x')
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position(('data', 0)) 
plt.title('Gráfica de $f(x) = (x + 2)^2$')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(x, y, color='g', label='$f(x) = x^2$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 
plt.xlabel('x')
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position(('data', 0)) 
plt.title('Gráfica de $f(x) = x^2$')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(x, y_right, color='b', label='$f(x) = (x - 2)^2$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 
plt.xlabel('x')
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position(('data', 0)) 
plt.title('Gráfica de $f(x) = (x - 2)^2$')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
