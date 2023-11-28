from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange
from math import ceil, log


start_time = time.time()

def tri_number(n):

    num = 1
    m = 2

    if n==1:
        return num
    else:
        for ii in range(n-1):
            num = num+m
            m+=1
        return num

def solution(n):

    return (n * (n * (4 * n + 3) + 8) - 9) / 6

def main():

    print(solution(1001))



if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))