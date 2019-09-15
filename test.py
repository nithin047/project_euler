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

	print(digits)
	print(digits.reverse())

	return (digits == digits.reverse())



def main():

	check_prod_palindrome(111, 9)



if __name__ == "__main__":
	main()

print("Runtime: %s" % (time.time() - start_time))