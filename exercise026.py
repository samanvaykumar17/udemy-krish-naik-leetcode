"""
Count Number of Odd and Even Elements in a List

Problem Description:

You are given a list of integers. Write a Python program that counts and returns the number of even and odd numbers in the list.

Example:

Input: lst = [1, 2, 3, 4, 5]
Output: (2, 3)
"""

def count_even_odd(lst):
    odd = 0
    even = 0
    
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even += 1 
        else:
            odd += 1 
            
    return (even, odd)
            
