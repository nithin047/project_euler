from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

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

    x = np.linspace(1, 1e6)
    plt.plot(x, x)
    plt.plot(x, (9**5)*(np.ceil(np.log10(x))))
    plt.show()



if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))