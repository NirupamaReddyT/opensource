#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Write your code here
    l=len(arr)
    p,n,z=0,0,0
    for i in arr:
        if i<0:
            n+=1
        elif i>0:
            p+=1
        else:
            z+=1
    print(p/l)
    print(n/l)
    print(z/l)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
