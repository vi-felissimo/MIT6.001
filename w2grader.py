'''
The area of a regular polygon is:  0.25∗𝑛∗𝑠2𝑡𝑎𝑛(𝜋/𝑛) 
The perimeter of a polygon is: length of the boundary
    of the polygon

Write a function called polysum that takes 2 arguments, n and s. 
    This function should sum the area and square of the perimeter
    of the regular polygon. The function returns the sum, rounded 
    to 4 decimal places.
'''

import math as m
def polyarea(n,s):
    return 0.25*n*s*s/(m.tan(m.pi/n))

def perimeter(n,s):
    return n*s

def polysum(n,s):
    return round(polyarea(n,s) + perimeter(n,s)**2, 4)

print('%.5f' % polysum(4,1))
    