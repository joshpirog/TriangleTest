# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Joshua Pirog
@author: rk
"""
#Classifies a triangle based on its properties
def classifyTriangle(a,b,c):
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'  
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'   
    if a == b and b == a:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) or ((b ** 2) + (c ** 2)) == (a ** 2):
        return 'Right'
    elif (a != b) and  (a != c) and (b != c):
        return 'Scalene'
    else:
        return 'Isosceles'
