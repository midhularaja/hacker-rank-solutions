#Problem: mini-max-sum
#Link: https://www.hackerrank.com/challenges/mini-max-sum/problem
#Difficulty: Easy
 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
     min_value = min(arr)
     max_value = max(arr)
     total= sum(arr)
     print(total-max_value,total-min_value)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
