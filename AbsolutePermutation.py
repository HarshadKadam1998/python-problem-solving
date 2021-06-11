"""
Absolute Permutation:
The problem-statement can be accessed using following link --->
https://www.hackerrank.com/challenges/absolute-permutation
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Write your code here
    l=[None]*(n+1)
    
    if k==0:
        return [i for i in range(1,n+1)]
    
    if (n%(2*k)!=0):
        return [-1]
    
    for i in range(1,n+1):
        if l[i]==None:
            l[i]=i+k
            l[i+k]=i
    return l[1:]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
