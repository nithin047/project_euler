from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange

start_time = time.time()

def sum_factors(n):

    original_n = n
    fsum = 1
    prime = 2

    while n>1:

        count = 0
        while n%prime==0:

            count = count+1
            n = n/prime

        fsum = fsum * (prime**(count+1) - 1)/(prime - 1)

        if prime == 2:
            prime+=1
        else:
            prime+=2

    return (fsum - original_n)

def main():

    numbers_to_check = np.linspace(1, 28123, 28123)
    numbers_to_check = numbers_to_check.tolist()
    abundant = []
    numbers_to_remove = []
    
    for ii in trange(1, 28124):

        if ii < sum_factors(ii):
            abundant.append(ii)

    abundant = np.sort(abundant)

    for ii in trange(len(abundant)):
        for jj in trange(len(abundant)):

            temp_sum = abundant[ii] + abundant[jj]

            if  temp_sum> 28123:
                break
            else:
                numbers_to_remove.append(temp_sum)

    numbers_to_remove = np.unique(numbers_to_remove)

    final_list = [x for x in numbers_to_check if x not in numbers_to_remove]

    print(np.sum(final_list))


    
    

if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))