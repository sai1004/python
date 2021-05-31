'''
    different ways of importing 
    1. import maths   // file name
    2. from maths import multiply  // importing specific function
    3. from maths import multiply , sub , sum  // importing multiple functions
    4. from maths import * // importing all the functions in maths module

'''

# using (4)
from maths import *


sum_of_ele = sum(1, 2)

print("sum: ", sum_of_ele)


sub_of_ele = sub(2, 1)

print("sub: ", sub_of_ele)


multi_of_ele = multiply(2, 3)

print("multiply: ", multi_of_ele)

square_of_ele = square(3)

print("square:", square_of_ele)


area_of_circle = area(10)

print("area_of_circle: ", area_of_circle)


circumfr = circumference(12)

print("circumfr: ", circumfr)


title_of_mathmodule = title()

print("title_of_mathmodule: ", title_of_mathmodule)
