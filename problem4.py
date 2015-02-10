#!/usr/bin/env python

from math import pow

def is_palindrone(num):
  num_array = []
  while num != 0:
    num_array.append(num%10)
    num = num/10
  for i in range(0,len(num_array)/2):
    if num_array[i] != num_array[-1-i]:
      return False
  return True

#brute force
def basic_concept(n):
  current_max = 0
  for i in range(int(pow(10,n-1)),int(pow(10,n))):
    for j in range(int(pow(10,n-1)),int(pow(10,n))):
      num = i*j
      if is_palindrone(num):
        if num > current_max:
          current_max = num
  return current_max

#ENHANCE!
def make_it_faster(n):
  current_max = 0
  for i in range(int(pow(10,n-1)),int(pow(10,n))):
    #don't check twice. don't check 1x2 then again 2x1
    for j in range(i,int(pow(10,n))):
      num = i*j
      #only check if already greater than max
      if num > current_max:
        if is_palindrone(num):
          current_max = num
  return current_max 

print make_it_faster(3)
#print basic_concept(3)
  
