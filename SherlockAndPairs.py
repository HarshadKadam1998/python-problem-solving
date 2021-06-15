"""
Sherlock and Pairs:
The problem-statement can be accessed using following link --->
https://www.hackerrank.com/challenges/sherlock-and-pairs
"""




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    # Write your code here
    a.sort()
    ans=0
    
    i=len(a)-1
    count=1
    while i>0:
        if a[i]==a[i-1]:
            count+=1
        else:
            ans+=count*(count-1)
            count=1    
        i-=1
    ans+=count*(count-1)
    return ans    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)

        fptr.write(str(result) + '\n')

    fptr.close()
