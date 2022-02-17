# any()
#This expression returns True if any element of the iterable is true.If the iterable is empty, it will return False.
# print(any([False, False, True, False]))
# print(any([1>0,1==0,1<0]))
# print(any([1<0,2<1,3<2]))

# all()
# This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.
# print(all(['a'<'b','b'<'c']))
# print(all(['a'<'b','c'<'b']))

# x = int(input("Number of Integers"))
# list = []
# string = ""
# for i in range(0,x):
#     taken = input()
#     list.append(taken)
#     string = string + " " + taken
#
# print(list)
# print(string)

# x = int(input("Number of Integers"))
# list = []
# list2 = []
# if 0 < x < 100:
#     string = input("Enter space seperated integers: ")
#     # print(type(string))
#     # print(string)
#     list2 = string.split(" ")
#     for i in range(0, x):
#         list.append(string[i])
#     # print(list)
#     # print(list2)
#
#     # Condition Part
#     if all(int(i)>0 for i in list2):
#         print("True")
#     else:
#         print("False")
#
# else:
#     print("Invalid Input")

import math


# def rev(num):
#     return int(num != 0) and ((num % 10) * \
#                               (10 ** int(math.log(num, 10))) + \
#                               rev(num // 10))
# x=676
# if x == rev(x):
#     print("True")
# else:
#     print("False")
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import math


# def rev(num):
#     return int(num != 0) and ((num % 10) * \
#                               (10 ** int(math.log(num, 10))) + \
#                               rev(num // 10))
#
#
# x = int(input())
# list2 = []
# if 0 < x < 100:
#     string = input()
#     list2 = string.split(" ")
#     if all(int(i) > 0 for i in list2):
#         if x == rev(x):
#             print("True")
#     else:
#         print("False")
# else:
#     print("Invalid Input")

# Sol
# Enter your code here. Read input from STDIN. Print output to STDOUT
N,n = int(input()),input().split()
print(all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))