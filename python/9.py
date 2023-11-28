from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

start_time = time.time()
	
def find_triplet():
	
	a = 1

	while(a<1000):

		b=5

		while(b<1000):
			lhs = a*b + 5 * 10**5
			rhs = 10**3 * (a+b)
			if lhs == rhs:
				return a, b, np.sqrt(a**2 + b**2)

			b = b+5
		a = a+1


def main():

	print(np.prod(find_triplet()))

if __name__ == "__main__":
	main()

print("Runtime: %s" % (time.time() - start_time))