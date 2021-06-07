"""
Append and Delete:
The problem-statement can be accessed using following link --->
https://www.hackerrank.com/challenges/append-and-delete/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
#from goto import goto, label
#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    n=min(len(s),len(t))
    i=0
    ans=0 
    """ 
    if s==None :
        ans=len(t)
        goto .jp
    elif t==None:
        ans=len(s)
        goto .jp
    """    
    if (len(s)+len(t))< k:
        return "Yes"
    while i<n:
        if s[i]!=t[i]:
            ans=len(s[i:])+len(t[i:])
            break
        i+=1
    if i==n:
            ans=len(s[i:])+len(t[i:])
    #label .jp
    if ans <= k:
        if (k-ans)%2==0:
            return "Yes"
        else:
            return "No"
    else :
        return "No"
    
        

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
