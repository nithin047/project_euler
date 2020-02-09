from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

start_time = time.time()




def main():

    f = open("11.txt", 'r')

    lines = f.readlines()

    num_array = []
    
    for ii in range(len(lines)):

        temp = ([float(n) for n in lines[ii].strip().split()])
        num_array.append(temp)

    #horizontal
    max_horizontal = 0
    for ii in range(len(lines)):
        for jj in range(len(lines) - 3):
            max_horizontal = np.maximum(max_horizontal, num_array[ii][jj]*num_array[ii][jj+1]*num_array[ii][jj+2]*num_array[ii][jj+3])

    #vertical
    max_vertical = 0
    for ii in range(len(lines)-3):
        for jj in range(len(lines)):

            if num_array[ii][jj]*num_array[ii+1][jj]*num_array[ii+2][jj]*num_array[ii+3][jj] == 51267216:
                print(ii)
                print(jj)
                print(num_array[ii][jj])
                print(num_array[ii+1][jj])
                print(num_array[ii+2][jj])
                print(num_array[ii+3][jj])

            max_vertical = np.maximum(max_vertical, num_array[ii][jj]*num_array[ii+1][jj]*num_array[ii+2][jj]*num_array[ii+3][jj])

    #right-diagonal
    max_rdiagonal = 0
    for ii in range(len(lines)-3):
        for jj in range(len(lines) - 3):
            max_rdiagonal = np.maximum(max_rdiagonal, num_array[ii][jj]*num_array[ii+1][jj+1]*num_array[ii+2][jj+2]*num_array[ii+3][jj+3])

    #left-diagonal
    max_ldiagonal = 0
    for ii in range(3, len(lines)):
        for jj in range(0, len(lines)-3):
            max_ldiagonal = np.maximum(max_ldiagonal, num_array[ii][jj]*num_array[ii-1][jj+1]*num_array[ii-2][jj+2]*num_array[ii-3][jj+3])

    print(max_ldiagonal)
    print(max_rdiagonal)
    print(max_vertical)
    print(max_horizontal)

    #print(np.maximum(max1, max2))


if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))