from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

start_time = time.time()

def sum_3_5(lim):

	sum = 0

	for ii in range(lim):
		if ((ii)%3 == 0 or (ii)%5==0):

			sum = sum + ii

	return sum


def main():

	print(sum_3_5(int(sys.argv[1])))

if __name__ == "__main__":
	main()

print("Runtime: %s seconds" % (time.time() - start_time)) 