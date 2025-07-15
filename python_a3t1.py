# Task 1: Calculate Factorial Using a Function

# Method 1 - Without any module

num=int(input("Enter a number: "))

def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num - 1) # recursive

result=factorial(num)
print ("(without import) The factorial of", num, "is", result)

# Method 2 - Using module

import math

num1=int(input("Enter a number: "))

result = math.factorial(num1)
print("(with import) The factorial of", num1, "is", result)

# Method 3 - Using from and importing only factorial

from math import factorial

num2=int(input("Enter a number: "))

result = math.factorial(num2)
print("(with importing only factorial) The factorial of", num2, "is", result)

# Method 4 - Using from and importing all

from math import *

num3=int(input("Enter a number: "))

result = math.factorial(num3)
print("(with importing all) The factorial of", num3, "is", result)