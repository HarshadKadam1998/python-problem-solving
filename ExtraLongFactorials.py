"""
Extra Long Factorials:
The problem-statement can be accessed using following link --->
https://www.hackerrank.com/challenges/extra-long-factorials/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    ans =1
    while n>=1:
        ans*=n
        n-=1
    print(ans)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
