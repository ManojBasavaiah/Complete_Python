import numpy as np
import matplotlib.pyplot as plt

A = np.random.randn(100000)
print(A)
plt.hist(A, bins=100)
plt.show()

B = np.zeros((3, 3), dtype=int)
print(B)

L = []
for x in range(0, 100):
    L.append(x * 2)
print(L)
print(L[::-2])
print(L[:2])

L1 = list(range(0,10,2))
print(L1)
