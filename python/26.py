from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange
from math import ceil, log


start_time = time.time()

def recurrence_cycle(n):

    existing_digits = []
    remainder = -1
    count = 0
    dividend = 10**ceil(log(n, 10))

    while True:

        if dividend>n:

            remainder = dividend%n
            if remainder in existing_digits:
                break
            else:
                existing_digits.append(remainder)
                dividend = remainder * 10
                remainder = -1

        else:
            dividend = dividend * 10
            existing_digits.append(0)

        count+=1

    return count



def main():

    max_length = 0
    max_num = 0

    for ii in trange(1, 1001):

        if ii%2==0 or ii%5==0:
            pass
        else:
            temp_length = recurrence_cycle(ii)
            if temp_length>max_length:
                max_length = temp_length
                max_num = ii

    print(max_num)
    print(recurrence_cycle(623))

if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))