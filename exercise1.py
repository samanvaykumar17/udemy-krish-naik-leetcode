"""
Square of side 'N'
Problem Description: You are given an integer n. 
Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.

Input: 3
Output: ['***', '***', '***']
 
Input: 5
Output: ['*****', '*****', '*****', '*****', '*****']
"""

def generate_square(n):
    ml = []
    for i in range(n):
        il = ""
        for i in range(n):
            il += "*"
        ml.append(il)
    
    return ml
