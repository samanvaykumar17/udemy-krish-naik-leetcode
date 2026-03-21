
"""
Hollow Square of side 'N'

Problem Description:

You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', 
represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

Example:

Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']

"""

def generate_hollow_square(n):
    ml = []
    for i in range(n):
        if (i == 0) or (i == n-1):
            il = "*" * n
        else:
            pl = " " * (n-2)
            il = "*" + pl + "*"
        ml.append(il)            

    return ml
