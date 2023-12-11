import numpy as np
import matplotlib.pyplot as plt

A = np.random.randn(100000)
print(A)
plt.hist(A, bins=100)
plt.show()

B = np.zeros((3, 3), dtype=int)
print(B)
