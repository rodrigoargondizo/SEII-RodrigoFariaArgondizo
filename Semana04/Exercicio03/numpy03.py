import numpy as np, matplotlib.pyplot as plt

a1 = np.array([2, 4, 6, 8, 10])
print(a1[2])
print(a1[2:])
print(a1[:-2])
print(a1[1:-2])
print(a1[a1>3])

names = np.array(['Jim', 'Luke', 'Josh', 'Peter'])
first_letter_j = np.vectorize(lambda s: s[0])(names) == 'J'
print(names[first_letter_j])

print(a1[a1%4 == 0])
