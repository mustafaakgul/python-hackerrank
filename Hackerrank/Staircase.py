#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

# def staircase(n):
#     if n > 0 and n <= 100:
#         stair = n - 2
#         for stairs in range(1, n):
#             print(' ' * stair, '#' * stairs)
#             stair -= 1
#         print('#' * n)
#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     staircase(n)

# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

    if N >= 1 and N <= 100:
        if N % 2 == 1:
            print("Weird")
        else:
            if N>=2 and N<=5:
                print("Not Weird")
            elif N>=6 and N<=20:
                print("Weird")
            elif N>20:
                print("Not Weird")

        # elif N % 2 == 0  in range (2, 5):
        #     print("Not Weird")