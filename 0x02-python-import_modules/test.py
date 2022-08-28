#!/usr/bin/python3
"""
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result"""
"""
import sys

arglist = len(sys.argv) - 1
add = 0
for i in range(arglist):
    add += int(sys.argv[i+1])

print(add)"""
"""
import hidden_4

path = dir(hidden_4)
for i in path:
    if "_" not in i[0]:
        print(i)"""

# from variable_load_5 import a

# print(a)

#!/usr/bin/python3
import string
print(string.ascii_lowercase)


print(string.ascii_uppercase)

