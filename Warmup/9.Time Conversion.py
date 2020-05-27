#Time conversion | [Problem](https://www.hackerrank.com/challenges/time-conversion/problem)

#!/bin/python3

import os
import sys

def timeConversion(s):
    t = s.split(":")
    if s[-2:] == "PM":
        if t[0] != "12":
            t[0] = str(int(t[0])+12)
    else:
        if t[0] == "12":
            t[0] = "00"
    ntime = ':'.join(t)
    return str(ntime[:-2])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
