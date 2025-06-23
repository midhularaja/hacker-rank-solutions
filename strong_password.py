#Problem: strong-password
#Link: https://www.hackerrank.com/challenges/strong-password/problem
#Difficulty: Easy
 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    digit = lower = upper= special=0
    for char in password:
        if '0'<=char<='9':
            digit =1
        elif 'a'<=char<='z':
            lower=1
        elif 'A'<=char<='Z':
            upper =1
        elif char in '!@#$%^&*()-+ ' :
            special =1
    missing = 4-(digit+lower+upper+special)
    return max(6-n,missing)                  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
