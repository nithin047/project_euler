from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

start_time = time.time()

def largest_prime_factor(number):

	factor = 2

	while(1):

		if factor == number:
			break

		while(number%factor == 0):
			number = number/factor

		factor = factor + 1

	return factor


def main():

	print(largest_prime_factor(int(sys.argv[1])))


if __name__ == "__main__":
	main()

print("Runtime: %s" % (time.time() - start_time))