#Problem: equality in a array
#Link: https://www.hackerrank.com/challenges/equality-in-a-array/problem
#Difficulty: Easy

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    max_freq=0
    for num in set(arr):
        freq = arr.count(num)
        if freq>max_freq:
            max_freq=freq
    return len(arr)-max_freq        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
