"""
Sum of List Elements

Problem Description:

Write a Python function that calculates the sum of all elements in a given list of integers.

Example:

Input: numbers = [1, 2, 3, 4, 5]
Output: 15

Input: numbers = [10, -5, 7, 8, -2]
Output: 18

"""

def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum
