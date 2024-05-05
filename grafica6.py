import numpy as np
import matplotlib.pyplot as plt


def f_half_cos(x):
    return 0.5 * np.cos(x)

x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

y_half_cos = f_half_cos(x)

plt.figure(figsize=(12, 4))

plt.plot(x, y_half_cos, label='$f(x) = \\frac{1}{2} \cos(x)$', color='r')
plt.title('Gráfica de $f(x) = \\frac{1}{2} \cos(x)$')
plt.legend()
plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1)
plt.grid(True)

plt.tight_layout()
plt.show()
