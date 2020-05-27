#Grading Students | [Problem](https://www.hackerrank.com/challenges/grading/problem)

#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    new_grades=[]
    for i in grades:
        if i>=38 and i%5!=0:
            n=i+5-i%5
            if n-i<3:
                new_grades.append(n)
            else:
                new_grades.append(i)
        else:
            new_grades.append(i)
    return new_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
