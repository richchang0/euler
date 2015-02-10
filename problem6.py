#!/usr/bin/env python

from math import pow

def brute(n):
	sum_of_squares = sum(map(lambda x : x*x, range(1,n+1)))
	square_of_sum = pow(sum(range(1,n+1)), 2)
	return square_of_sum - sum_of_squares

print brute(100)