"""
Check if all elements in a list are Unique

Problem Description:

You are given a list of integers. 
Write a Python program that checks if all elements in the list are unique. 
If all elements are unique, return True; otherwise, return False.

Example:

Input: lst = [1, 2, 3, 4, 5]
Output: True

Input: lst = [1, 2, 3, 3, 4, 5]
Output: False
"""

def check_unique(lst):
    unique_list = []
    for i in range(len(lst)):
        present = False
        
        for j in range(len(unique_list)):
            if lst[i] == unique_list[j]:
                present = True
                return False
        
        if not present:
            unique_list.append(lst[i])
    
    return True
