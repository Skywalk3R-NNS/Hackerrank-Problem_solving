#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    # Write your code here
    candymap = [1]*n
    for i in range(1,n):
        if arr[i-1] > arr[i] and candymap[i-1] <= candymap[i]:
            candymap[i-1] = candymap[i]+1
        elif arr[i] > arr[i-1] and candymap[i] <= candymap[i-1]:
            candymap[i] = candymap[i-1]+1
    for i in range(n-2,-1,-1):
        if arr[i] > arr[i+1] and candymap[i] <= candymap[i+1]:
            candymap[i] = candymap[i+1]+1
    return sum(candymap)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
