import numpy as np
import matplotlib.pyplot as plt

# Definir la función original
def f(x):
    return x**2

# Definir la función desplazada dos unidades a la izquierda
def f_left(x):
    return (x + 2)**2

# Definir la función desplazada dos unidades a la derecha
def f_right(x):
    return (x - 2)**2

# Generar datos para x
x = np.linspace(-5, 5, 400)

# Calcular los valores de las funciones para los datos de x
y = f(x)
y_left = f_left(x)
y_right = f_right(x)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y_left, color='r', label='$f(x) = (x + 2)^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Desplazamiento a la izquierda')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(x, y, color='b', label='$f(x) = x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función original')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(x, y_right, color='g', label='$f(x) = (x - 2)^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Desplazamiento a la derecha')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
