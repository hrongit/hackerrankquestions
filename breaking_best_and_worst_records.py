#question - https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def getRecord(s):
    highest_score = 0
    lowest_score = 0
    count_highest = 0
    count_lowest = 0
    for i in range(len(s)):
        if i == 0:
            highest_score = lowest_score = s[i]
        elif s[i] > highest_score:
            highest_score = s[i]
            count_highest += 1
        elif s[i] < lowest_score:
            lowest_score = s[i]
            count_lowest += 1
    
    return count_highest, count_lowest

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
