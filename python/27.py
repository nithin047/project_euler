from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange
from math import ceil, log


start_time = time.time()

def prime_upper_bound(n):

    upper_bound = n * (np.log(n) + np.log(np.log(n)))

    return int(np.ceil(upper_bound))

def erato_sieve(n):

    upper_bound = prime_upper_bound(n)
    #print(upper_bound)
    is_prime = np.ones(upper_bound+1)
    p = 2

    #begin the Sieve

    while(p*p < upper_bound):

        #print(p)

        index = p*p

        while(index <= upper_bound):

            is_prime[index] = 0
            index = index + p

        nonzero_indices = np.nonzero(is_prime)

        #print(nonzero_indices)

        for ii in range(len(nonzero_indices[0])):
            if p < nonzero_indices[0][ii]:
                p = nonzero_indices[0][ii]
                break

    final_nonzero_indices = np.nonzero(is_prime)

    prime_list = final_nonzero_indices[0].tolist()
    del prime_list[0]
    del prime_list[0]

    return prime_list


def main():

    primes_1e3 = erato_sieve(1000)
    del primes_1e3[0]
    primes_1e3 = np.asarray(primes_1e3)

    prime_list = erato_sieve(100000)
    prime_list = set(prime_list)
    
    a_array = np.linspace(-999, 999, 1999)
    b_array = primes_1e3[primes_1e3<1000]

    n_max = 0
    a_max = 0
    b_max = 0

    for ii in trange(len(a_array)):
        for jj in trange(len(b_array)):
            count = 0
            n = 0
            while True:
                q = n**2 + a_array[ii]*n + b_array[jj]
                
                if q in prime_list:
                    count = count+1
                    n = n+1
                else:
                    if n>n_max:
                        n_max = n
                        a_max = a_array[ii]
                        b_max = b_array[jj]
                    break
    print(a_max)
    print(b_max)

if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))