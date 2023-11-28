from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange

start_time = time.time()

def main():
    
    f = open("18.txt", 'r')
    lines = f.readlines()
    tri_array = np.zeros((len(lines), len(lines)))

    for ii in range(len(lines)):
        numbers = lines[ii].strip().split()
        for jj in range(len(numbers)):
            tri_array[ii, jj] = int(numbers[jj])

    for ii in trange(len(lines)-1, 0, -1):
        for jj in trange(ii):
            tri_array[ii-1, jj] = tri_array[ii-1, jj] + np.maximum(tri_array[ii, jj], tri_array[ii, jj+1])

    print(tri_array[0][0])
    



if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))