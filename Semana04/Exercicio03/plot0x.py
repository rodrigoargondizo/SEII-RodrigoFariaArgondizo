import matplotlib.pyplot as plt, numpy as np

x = range(1, 11)
y = range(1, 11)

plt.scatter(x, y)

x1 = np.arange(-1000, 1000, 1)

plt.plot(x1, x1**2)
plt.show()
