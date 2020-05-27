#Staircase | [Problem](https://www.hackerrank.com/challenges/staircase/problem)

#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    for i in range(1,n+1):
        print(" "* (n-i)+ "#" *i)

if __name__ == '__main__':
    n = int(input())
    staircase(n)
