from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange

start_time = time.time()

def fact(n):

    ans = 1
    for ii in range(1, n+1):
        ans = ans * ii

    return ans

def sum_digits(n):

    sum = 0

    while n>0:
        sum = sum + n%10
        n=n//10

    return sum

def main():
    
    print(sum_digits(fact(100)))

    



if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))