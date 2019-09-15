from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
import time
import sys

start_time = time.time()

def read_file():

	f = open("8.txt", 'r')
	array = f.read()
	f.close()
	return array

def generate_possibilities():

	master_string = read_file()

	int_list = []

	for ii in master_string:

		int_list.append(int(ii))

	#print(int_list)

	possible = []

	index = 0

	while (index <= len(int_list) - 14):

		possible.append(int_list[index:index+13])

		index = index + 1

	possible.append(int_list[index:])

	#print(possible)

	return possible

def clean_up():

	possible = generate_possibilities()
	cleaned_possible = []

	for ii in possible:
		if(len(np.nonzero(ii)[0]) == 13):
			cleaned_possible.append(ii.copy())

	return cleaned_possible

def max_product():

	cleaned = clean_up()

	prod = 1

	for ii in cleaned:
		test = 1
		for jj in ii:
			test = test*jj

		if test>prod:
			prod = test
	return prod


def main():

	print(max_product())

if __name__ == "__main__":
	main()

print("Runtime: %s" % (time.time() - start_time))