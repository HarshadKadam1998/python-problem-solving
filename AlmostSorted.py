"""
Almost Sorted:
The problem-statement can be accessed using following link --->
https://www.hackerrank.com/challenges/almost-sorted
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    output=0
    trac=0
    templ=[]
    templ.extend(arr)
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            trac=i
            break
        if i+2==len(arr):
            print("yes")
            output=1
    
    m=arr.index(min(arr[trac:len(arr)]))
    swap=arr[trac]
    arr[trac]=arr[m]
    arr[m]=swap
    trac1=0
    for i in range(len(arr)-1):
        if output!=0:
            break
        if arr[i]>arr[i+1]:
            trac1=i
            break
        if i+2==len(arr):
            print("yes")
            print("swap {0} {1}".format(trac+1,m+1))
            output=1
            
    if trac1!=0:
        templ2=templ[trac:m+1]
        templ2.reverse()
        z=trac
        for i in range(len(templ2)):
            templ[z]=templ2[i]
            z+=1
        for i in range(len(templ)-1):
            if templ[i]>templ[i+1]:
                break
            if i+2==len(templ):
                print("yes")
                print("reverse {0} {1}".format(trac+1,m+1))
                output=1    
    if output==0:
        print("no")        
        
        
        
        
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)

