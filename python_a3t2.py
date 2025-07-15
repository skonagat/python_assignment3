# Task 2: Using the Math Module for Calculations

# Method 1 - Using import

import math

num = float(input("Enter a number: "))

def square_root (num):
    return math.sqrt(num)
def logarithm (num):
    return math.log(num)
def sin (num):
    return math.sin(num)

result_square_root = square_root(num)
result_logarithm = logarithm(num)
result_sin = sin(num)

print("The square root of ", num, "is", result_square_root)
print("The logarithm of ", num, "is", result_logarithm)
print("The sin of ", num, "is", result_sin)

#This is as good as calling results directly using "math" as below.
print("The square root of ", num, "is", math.sqrt(num))
print("The logarithm of ", num, "is", math.log(num))
print("The sin of ", num, "is", math.sin(num))

# Method 2 - Using from and importing specific modules

from math import sqrt, log, sin

num1 = float(input("Enter a number: "))

print("Square root of num1 is", sqrt(num1))
print("Logarithm of num1 is", log(num1))
print("Sin of num1 is", sin(num1))

# Method 3 - Using from and importing all modules

from math import *

num2 = float(input("Enter a number: "))

print("Square root of num1 is", sqrt(num2))
print("Logarithm of num1 is", log(num2))
print("Sin of num1 is", sin(num2))