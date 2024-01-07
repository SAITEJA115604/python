# Replace all odd numbers in the given array with -1
################input###########################
import numpy as np
l = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
even = 0
odd = 0
even_numbers=[]
odd_numbers=[]
for i in range(len(l)):
    if l[i]%2 != 0:
        l[i]= -1
print("The array after replacing odd numbers with -1:", end=" ")
print(l)
