from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange

start_time = time.time()

def sum_digits(n):

    sum = 0

    while n>0:
        sum = sum + n%10
        n = n//10
    return sum

def main():

    s = pow(2, 1000)
    print(sum_digits(pow(2, 15)))
    print(sum_digits(s))



if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))