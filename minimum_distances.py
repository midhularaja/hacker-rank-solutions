#Problem: minimum distances
#Link: https://www.hackerrank.com/challenges/minimum-distances/problem
#Difficulty: Easy
 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    ans=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                value = abs(j-i)
                ans.append(value)
    if ans:
        return min(ans)
    else:
        return -1                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
