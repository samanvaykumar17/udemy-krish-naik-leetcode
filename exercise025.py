"""
Program to Reverse a List

Problem Description:

You are given a list of integers. 
Write a Python program that reverses the list without using slicing (lst[::-1]). 
The program should return the reversed list.

Example:

Input: lst = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""

def reverse_list(lst):
    reverse = []
    
    for i in range(len(lst), 0, -1):
        print(i)
        reverse.append(lst[i-1])
    
    return reverse
