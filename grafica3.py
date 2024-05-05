import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x
def f_minus(x):
    return -x

x = np.linspace(-5, 5, 100)

y = f(x)
y_minus = f_minus(x)

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y, label='$f(x) = x$', color='b')
plt.title('Gráfica de $f(x) = x$')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 
plt.gca().spines['left'].set_position('center')
plt.gca().spines['bottom'].set_position('center')
plt.xticks(np.arange(-5, 6, 1))
plt.yticks(np.arange(-5, 6, 1))
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, y_minus, label='$f(x) = -x$', color='r')
plt.title('Gráfica de $f(x) = -x$')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1) 
plt.gca().spines['left'].set_position('center')
plt.gca().spines['bottom'].set_position('center')
plt.xticks(np.arange(-5, 6, 1))
plt.yticks(np.arange(-5, 6, 1))
plt.grid(True)

plt.tight_layout()
plt.show()
