# Find the positions of:elements in x where its value is more than its corresponding element in y, and elements in x where its value is equals to its corresponding element in y.
import numpy as np
x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89]) 
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])
position= np.where(x>y)
print(position)
