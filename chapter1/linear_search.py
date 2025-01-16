#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:19:46 2025

@author: fawaz
"""

def linear_search(array,x):
    for i in range(len(array)):
        if array[i]==x:
            print(f"found match at position {i}")
            break;
        if i == (len(array)-1):
            print("No match found")
        
        

array = [1,2,3,4,5,10]
x = 3 
linear_search(array,x)
            
    
            