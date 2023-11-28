from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange

start_time = time.time()

def main():

    filename = '22.txt'
    f = open(filename, 'r')
    lines = f.readlines()
    names = lines[0].split(",")
    cleaned_names = []

    for name in names:
        cleaned_names.append(name.strip('"'))

    cleaned_names.sort()

    sum = 0

    for ii in trange(len(cleaned_names)):

        name = cleaned_names[ii]
        name_value = 0
        for letter in name:
            value = ord(letter) - 64
            name_value+=value
        sum += name_value * (ii+1) 

    print(sum)

    
    

if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))