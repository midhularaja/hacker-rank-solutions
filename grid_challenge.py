#Problem: grid challenge
#Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem
#Difficulty: Easy

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    sorted_rows=[''.join(sorted(row)) for row in grid]
    columns=zip(*sorted_rows)
    for col in columns:
        if list(col)!=sorted(col):
            return "NO"
    return "YES"        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
