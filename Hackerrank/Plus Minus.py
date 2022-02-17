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
    count_positive = 0
    count_negative = 0
    count_zero = 0

    for i in range(0, len(arr)):
        if arr[i] < 0:
            count_negative += 1
        elif arr[i] > 0:
            count_positive += 1
        else:
            count_zero += 1

    print(count_positive, count_negative, count_zero)

    print(round(float(count_positive / len(arr)), 6))
    print(round(float(count_negative / len(arr)), 6))
    print(round(float(count_zero / len(arr)), 6))





if __name__ == '__main__':
    #inputs
    #6
    # -4 3 -9 0 4 1
    # n = int(input().strip())
    #
    # arr = list(map(int, input().rstrip().split()))
    #
    # plusMinus(arr)

    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
