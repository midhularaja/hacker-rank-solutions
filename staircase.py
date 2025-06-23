#Problem: staircase
#Link: https://www.hackerrank.com/challenges/staircase/problem
#Difficulty: Easy
 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts an INTEGER n as a parameter.
#

def staircase(n):
    # Write your code here
    for i in range(n):
        for k in range(n-i-1):
           print ("",end=" ")
        for j in range (i+1):
            print("#",end="") 
        print ()
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
