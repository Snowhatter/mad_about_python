#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findNumber(arr, k):
    # Write your code here
    if k in arr:
        print('YES')
    else:
        print('NO')

numarray=[]
element_count=0
search_element=0
n = 0

#print('enter number of elements in a random array of your choice')
element_count=int(input())

#print('enter elements in array')
while element_count > n: 
    numarray.append(int(input()))
    n = n + 1

#print('enter an element to be searched within array')
search_element = int(input())

findNumber(numarray, search_element)
