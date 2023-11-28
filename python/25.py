from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange


start_time = time.time()

def main():

    num1 = 1
    num2 = 1
    index = 2
    while int(num2//10**999 == 0):

        temp = num2
        num2 = num1 + num2
        num1 = temp
        index+=1

    print(index)



if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))