#Mini-max-Sum | [Problem](https://www.hackerrank.com/challenges/mini-max-sum/problem)

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    m=sum(arr)
    print(m-max(arr),m-min(arr))
