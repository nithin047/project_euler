from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange
from scipy.special import factorial

start_time = time.time()

def main():

    limit = 999999
    num_range = 9
    number = []
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for ii in range(num_range, -1, -1):
        index = int(limit//factorial(ii))
        print(index)
        print(digits)
        number.append(digits[index])
        del digits[index]
        limit = limit - index * factorial(ii)

    print(number)


if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))