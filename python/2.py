from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

start_time = time.time()

def even_fibonacci(limit):

	sum_even = 0

	prev_1 = 1
	prev_2 = 1

	curr = 2

	while(curr <= limit):

		if curr%2 == 0:

			sum_even = sum_even + curr

		prev_1=prev_2
		prev_2 = curr
		curr = prev_1 + prev_2

	return sum_even




def main():

	print(even_fibonacci(int(sys.argv[1])))

if __name__ == "__main__":
	main()

print("Runtime: %s seconds" % (start_time - time.time()))