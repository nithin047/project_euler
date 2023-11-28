from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

start_time = time.time()

def diff_sum_sq(n):

	return (n*(n+1)/2)**2 - n*(n+1)*(2*n + 1)/6

def main():

	print(diff_sum_sq(int(sys.argv[1])))

if __name__ == "__main__":
	main()

print("Runtime: %s" % (time.time() - start_time))