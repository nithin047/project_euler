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

    return (seq)


def main():

    max_len = 1
    max_num = 1

    for ii in trange(8, 1000001):
        
        seq = collatz(ii)
        if max_len < len(seq):
            max_len = len(seq)
            max_num = ii


    print(max_len)
    print(max_num)

    



if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))