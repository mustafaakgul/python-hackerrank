#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    arr_rvr = ""
    for i in reversed(arr):
        arr_rvr += str(i) + " "

    print(arr_rvr)
