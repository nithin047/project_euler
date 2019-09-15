from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

start_time = time.time()

def euclid_gcd(a, b):

	temp = 0

	if(a<b):

		temp = a
		a=b
		b=temp

	while(1):

		r = a%b

		if r==0:
			return b
		else:
			a=b
			b=r

def perfect_divisor(num):

	product = 1

	while(num>0):

		gcd = euclid_gcd(product, num)

		product = product * num / gcd

		num = num - 1

	return product


def main():

	print(perfect_divisor(int(sys.argv[1])))

if __name__ == "__main__":
	main()

print("Runtime: %s" % (time.time() - start_time))