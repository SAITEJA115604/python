# Convert a 1-D array into a 2-D array with 3 rows
import numpy as np
b = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
c =b.reshape(3,-1)
print(c)

