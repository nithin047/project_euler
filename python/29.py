from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange
from math import ceil, log


start_time = time.time()



def main():
    power = []

    for ii in range(2, 101):
        for jj in range(2, 101):

            power.append(ii**jj)

    print(len(np.unique(power)))


if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))