#Problem: separate the numbers
#Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem
#Difficulty: Easy

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    n=len(s)
    for length in range(1,n):
        first = int(s[:length])
        num=first
        seq=""
        while len(seq)<n:
            seq += str(num)
            num+=1
        if seq==s:
            print("YES",first)
            return
    print("NO")            
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
