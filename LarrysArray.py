'''
Larry's Array:
The problem-statement can be accessed using following link --->
https://www.hackerrank.com/challenges/larrys-array
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

    
    
def larrysArray(A):
    # Write your code here
    return "YES" if sum([1 for i in range(len(A)) for j in range(i+1,len(A)) if A[i]>A[j]]) %2==0 else "NO"
                
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
