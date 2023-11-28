from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

start_time = time.time()

def check_prod_palindrome(a, b):

	prod = a*b

	digits = []

	while(prod!=0):
		digits.append(prod%10)
		prod = prod//10

	rev_digits = digits.copy()
	rev_digits.reverse()

	return (digits == rev_digits)



def main():

	max = 0

	for ii in range(1000):
		for jj in np.arange(0, 1000, 11):

			if(check_prod_palindrome(ii, jj)):
				if ii*jj > max:
					max = ii*jj


	print(max)


if __name__ == "__main__":
	main()

print("Runtime: %s" % (time.time() - start_time))