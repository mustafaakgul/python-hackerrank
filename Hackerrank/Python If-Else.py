#!/bin/python3


import math
import os
import random
import re
import sys

# if __name__ == '__main__':
#     N = int(input().strip())
#
#     if N >= 1 and N <= 100:
#         if N % 2 == 1:
#             print("Weird")
#         else:
#             if N >= 2 and N <= 5:
#                 print("Not Weird")
#             elif N >= 6 and N <= 20:
#                 print("Weird")
#             elif N > 20:
#                 print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())

    if n >= 1 and n <= 100:
        if n % 2 == 1:
            print("Weird")
        elif n % 2 == 0 and n in range(2, 6):
            print("Not Weird")
        elif n % 2 == 0 and n in range(6, 21):
            print("Weird")
        elif n % 2 == 0 and n > 20:
            print("Not Weird")
