import numpy as np, matplotlib.pyplot as plt

a1 = np.array([3, 5, 7, 3])

print(2*a1)
print(1/a1)
print(a1>4)
print(a1[a1>4])
print(1/a1 + a1 + 2)
print(np.linspace(0, 1, 10)**2)

x = np.linspace(0, 1, 10)
y = x**2
plt.plot(x, y)
plt.show()

def f(x):
    return x**2 * np.sin(x) / np.exp(-x)

print(f(x))
