from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange

start_time = time.time()

def factorize(n):

    original_n = n
    num_factors = 1
    factor = 1
    factor_list = []

    while factor <= int(np.sqrt(original_n)) + 1:

        if n%factor == 0:
            if factor in factor_list:
                factor = factor + 1
            else:
                factor_list.append(factor)
                factor_list.append(int(original_n/factor))
        else:
            factor = factor + 1

    return factor_list, len(factor_list)



def main():

    for ii in trange(10000, 20000):

        tri = ii*(ii+1)/2
        _, num_factors = factorize(tri)

        if num_factors > 500:
            print(tri)

if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))