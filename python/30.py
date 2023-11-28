from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange
from math import ceil, log


start_time = time.time()

def sum_digit_power(n):

    sum_digit = 0

    while n>0:

        digit = n%10
        sum_digit = sum_digit + digit**5
        n=n//10
    return sum_digit


def main():

    big_sum = 0
    
    for ii in trange(2, int(1e6)):

        if sum_digit_power(ii) == ii:
            big_sum = big_sum + ii

    print(big_sum)


if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))