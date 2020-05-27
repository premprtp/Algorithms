#Compare the triplets | [Problem](https://www.hackerrank.com/challenges/plus-minus/problem)

#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    neg=0
    pos=0
    zero=0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zero+=1
    print("{0:.6f}".format(abs(pos/n)))
    print("{0:.6f}".format(abs(neg/n)))
    print("{0:.6f}".format(abs(zero/n)))
       
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
