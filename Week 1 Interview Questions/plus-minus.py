#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pc=0
    nc=0
    zc=0
    for i in arr:
        if(i>0):
            pc+=1
        elif(i<0):
            nc+=1
        else:
            zc+=1
    print("{:.6f}".format(pc/(pc+nc+zc)))
    print("{:.6f}".format(nc/(pc+nc+zc)))
    print("{:.6f}".format(zc/(pc+nc+zc)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
