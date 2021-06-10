'''
3D Surface Area:
The problem-statement can be accessed using following link --->
https://www.hackerrank.com/challenges/3d-surface-area
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    H=len(A)
    W=len(A[0])
    i,j=0,0;
    #tlist=[[0 for i in range(H+2)]for j in  range(W+2)]
    tlist=[]
    for i in range(H+2):
        t=[]
        for j in  range(W+2):
            if (i>0 and j>0) and (i<H+1 and j<W+1):
                t.append(A[i-1][j-1])
            else:
                t.append(0)
        tlist.append(t)
 
    i,j=1,1;      
    '''      
    for i in range(H+1):
        for j in  range(W+1):
            tlist[i][j]=A[i-1][j-1]
            #tlist[i].insert(j,A[i-1][j-1])  
    '''                    
    i,j=1,1;
    ans = 2*H*W
    for i in range(H+1):
        for j in  range(W+1):
            if  tlist[i][j]>tlist[i-1][j]: 
                ans+=tlist[i][j]-tlist[i-1][j]
            if  tlist[i][j]>tlist[i+1][j]: 
                ans+=tlist[i][j]-tlist[i+1][j]
            if  tlist[i][j]>tlist[i][j-1]: 
                ans+=tlist[i][j]-tlist[i][j-1] 
            if  tlist[i][j]>tlist[i][j+1]: 
                ans+=tlist[i][j]-tlist[i][j+1]            
    
    return ans;
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
