#Problem: mars exploration
#Link: https://www.hackerrank.com/challenges/three-month-preparation-kit-mars-exploration/problem
#Difficulty: Easy
 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    expected_value="SOS"
    count=0
    for i in range(len(s)):
        if s[i]!=expected_value[i%3]:
            count+=1
    return count        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
