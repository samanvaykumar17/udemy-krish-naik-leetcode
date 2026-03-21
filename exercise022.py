"""
Largest Element in a List

Problem Description:

Write a Python function that finds and returns the largest element in a given list of integers.

Example:

Input: numbers = [3, 8, 2, 10, 5]
Output: 10

Input: numbers = [-5, -10, -2, -1, -7]
Output: -1
"""

def find_largest(numbers):
    largest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest
