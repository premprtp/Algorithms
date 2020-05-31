#Apple and Orange | [Problem](https://www.hackerrank.com/challenges/apple-and-orange/problem)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count=0
    orange_count=0
    for i in apples:
        if (a+i>=s) and (a+i<=t):
            apple_count+=1
    for i in oranges:
        if (b+i>=s) and (b+i<=t):
            orange_count+=1
    print (apple_count,orange_count,sep="\n")


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
