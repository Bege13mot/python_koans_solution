#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    if min([a, b, c]) <= 0:
           raise TriangleError

    if sorted([a,b,c])[0]+sorted([a,b,c])[1]<=sorted([a,b,c])[2]:
        raise TriangleError

    set_a=set(([a,b,c]))
    if len(set_a)==1:
        return 'equilateral'
    elif len(set_a)==2:
        return 'isosceles'
    elif len(set_a)==3:
        return 'scalene'

    

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
