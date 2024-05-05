import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return np.abs(x - 2) + 3
def f2(x):
    return x**2 + 2*x
def f3(x):
    return np.sin(2*x) + np.pi

x = np.linspace(-10, 10, 400)
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(x, y1, label='$F(x) = |x - 2| + 3$', color='b')
plt.title('Gráfica de $F(x) = |x - 2| + 3$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(x, y2, label='$F(x) = x^2 + 2x$', color='r')
plt.title('Gráfica de $F(x) = x^2 + 2x$')
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.gca().spines['left'].set_position(('data', 0))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['top'].set_color('none')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(x, y3, label='$F(x) = \sin(2x) + \pi$', color='g')
plt.title('Gráfica de $F(x) = \sin(2x) + \pi$')
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
