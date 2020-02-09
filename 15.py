from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange

start_time = time.time()

def collatz(n):
    seq = []

    while n!=1:
        seq.append(n)
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n+1
    seq.append(1)

    return len(seq)


def main():

    len_seq = np.zeros(1000000)

    for ii in trange(500001, 1000001):
        
        len_seq[ii] = collatz(ii)
        


    



if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))