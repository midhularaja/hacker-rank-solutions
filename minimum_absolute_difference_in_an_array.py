#Problem: minimum-absolute-difference-in-an-array
#Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-minimum-absolute-difference-in-an-array/problem
#Difficulty: Easy
 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.


def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    ans=[]
    n=len(arr)
    for i in range(n-1):
        value = arr[i+1]-arr[i]
        ans.append(value)
    return min(ans)    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

