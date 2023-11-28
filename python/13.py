from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange

start_time = time.time()


def main():
    cumsum = 0
    f = open("13.txt", 'r')
    for ii in f.readlines():
        number = float(ii)
        cumsum = cumsum + number

    print(cumsum)

if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))