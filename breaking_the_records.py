#Problem: breaking_the_records
#Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/problem
#Difficulty: Easy
 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    max_score = scores[0]
    min_score =scores[0]
    max_count=0
    min_count=0
    for score in scores[1:]:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score< min_score:
            min_score =score
            min_count += 1
    return  max_count,min_count         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
