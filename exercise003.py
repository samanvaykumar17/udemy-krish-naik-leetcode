"""
Rectangle Pattern

Problem Description:

You are given two integers, n and m. 
Your task is to return a rectangle pattern of '*', 
where n represents the number of rows (length) and m represents the number of columns (breadth).

Example:

Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']
 
Input: n = 3, m = 2
Output: ['**', '**', '**']
"""


def generate_rectangle(n, m):
    ml = []
    for i in range(n):
        il = ""
        for i in range(m):
            il += "*"
        ml.append(il)
    
    return ml
