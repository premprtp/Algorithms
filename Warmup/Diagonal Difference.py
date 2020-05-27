#Compare the triplets | [Problem](https://www.hackerrank.com/challenges/diagonal-difference/problem)

#!/bin/python3

import math
import os
import random
import re
import sys

n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().strip().split())))

pri =0
sec=0
length = len(mat[0])
for i in range(length):
    pri += mat[i][i]
    sec += mat[i][(length-i-1)]
print(abs(pri-sec))