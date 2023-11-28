from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

start_time = time.time()

def prime_upper_bound(n):

	upper_bound = n * (np.log(n) + np.log(np.log(n)))

	return int(np.ceil(upper_bound))

def erato_sieve(n):

	upper_bound = prime_upper_bound(n)
	#print(upper_bound)
	is_prime = np.ones(upper_bound+1)
	p = 2

	#begin the Sieve

	while(p*p < upper_bound):

		#print(p)

		index = p*p

		while(index <= upper_bound):

			is_prime[index] = 0
			index = index + p

		nonzero_indices = np.nonzero(is_prime)

		#print(nonzero_indices)

		for ii in range(len(nonzero_indices[0])):
			if p < nonzero_indices[0][ii]:
				p = nonzero_indices[0][ii]
				break

	final_nonzero_indices = np.nonzero(is_prime)

	return(final_nonzero_indices[0][n+1])


def main():

	print(erato_sieve(int(sys.argv[1])))

if __name__ == "__main__":
	main()

print("Runtime: %s" % (time.time() - start_time))