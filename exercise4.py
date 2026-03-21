"""
Right Angled Triangle

Problem Description:

You are given an integer n. 
Your task is to return a right-angled triangle pattern of '*' where each side has n characters, 
represented as a list of strings. The triangle has '*' characters, 
starting with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.

Example:

Input: 3
Output: ['*', '**', '***']
 
Input: 5
Output: ['*', '**', '***', '****', '*****']
"""

def generate_triangle(n):
    ml = []
    
    for i in range(n):
        il = "*"
        for j in range(i):
            il += "*"        
        ml.append(il)
    
    return ml
        
