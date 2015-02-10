#!/usr/bin/env python

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

from math import pow

def find_largest_prime_factor(num):
  limit = int(pow(num, 0.5))
  for i in [2]+range(3,limit,2):
    if num % i == 0:
      num = num/i
      if num == 1:
        return i
print find_largest_prime_factor(600851475143)

