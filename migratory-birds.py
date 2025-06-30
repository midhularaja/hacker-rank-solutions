#Problem: migratory birds
#Link: https://www.hackerrank.com/challenges/migratory-birds/problem
#Difficulty: Easy

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    get_count_values=[]
    pick_bird=[]
    for i in set(arr):
        ans=arr.count(i)
        get_count_values.append((ans,i))
    max_count = max(get_count_values)[0]
    for count,value in get_count_values:
        if count==max_count:
            pick_bird.append(value)
    return (min(pick_bird))             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
