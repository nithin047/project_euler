from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange

start_time = time.time()

def sum_factors(n):

    list_factors = []
    list_factors.append(1)

    for ii in range(2, int(np.sqrt(n)+1)):
        if n%ii == 0:
            list_factors.append(ii)
            list_factors.append(n/ii)

    return int(np.sum(list_factors))

def main():
    
    checked = []
    amicable = []
    sum_factor_list = np.zeros(10001, dtype = int)
    for n in range(2, 10001):

        if sum_factor_list[n] != 0:
            d_n = sum_factor_list[n]
            if d_n >= 10000:
                d_d_n = sum_factors(d_n)
            else:
                if sum_factor_list[d_n] != 0:
                    d_d_n = sum_factor_list[d_n]
                else:
                    d_d_n = sum_factors(d_n)
                    sum_factor_list[d_n] = d_d_n

            if n == d_d_n and n!=d_n:
                amicable.append(n)
                if d_d_n <= 10000 and n!=d_n:
                    amicable.append(d_d_n)
        else:
            d_n = sum_factors(n)
            sum_factor_list[n] = d_n
            if d_n >= 10000:
                d_d_n = sum_factors(d_n)
            else:
                if sum_factor_list[d_n] != 0:
                    d_d_n = sum_factor_list[d_n]
                else:
                    d_d_n = sum_factors(d_n)
                    sum_factor_list[d_n] = d_d_n

            if n == d_d_n and n!=d_n:
                amicable.append(n)
                if d_d_n <= 10000 and n!=d_n:
                    amicable.append(d_d_n)


    print(np.unique(amicable))
    print(np.sum(np.unique(amicable)))

if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))