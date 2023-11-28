from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys
from tqdm import trange

start_time = time.time()

def main():
    
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #Sunday is 0 mod 7
    indicator = 1
    indicator = (indicator + 365)%7
    sunday_count = 0

    for ii in range(1901, 2001):
        if ii%4==0:
            if ii%100 == 0:
                if ii%400 == 0:
                    is_leap = 1
                else:
                    is_leap = 0
            else:
                is_leap = 1
        else:
            is_leap = 0

        if is_leap == 0:
            use_days = days
        else:
            use_days = leap_days

        for num_days in use_days:
            if indicator==0:
                sunday_count = sunday_count+1
            indicator = (indicator + num_days)%7

    print(sunday_count)

    



if __name__ == "__main__":
    main()

print("Runtime: %s" % (time.time() - start_time))