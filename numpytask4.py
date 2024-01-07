# Generate a 1-D array of 10 random integers. Each integer should be a number between 30 and 40 (inclusive)
import numpy as np
from numpy.random import randint
from numpy.random import seed
seed(1)
c= randint(30,40,10)
print(c)
