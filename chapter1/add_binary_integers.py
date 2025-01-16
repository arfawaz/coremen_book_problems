#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:57:08 2025

@author: fawaz
"""

def add_binary(array_1,array_2,n):
    sum = [0]*(n+1)
    carry = 0
    for i in range(n-1,-1,-1):
        print(f"i is {i}")
        print("kundi")
        c = array_1[i] + array_2[i] + carry
        if c == 2:
            carry = 1
            c = 0
            if i == 0:
                sum[0] = 1
        if c == 3:
            carry = 1
            c = 1
            if i == 0:
                sum[0] = 1
        
        sum[i+1] = c
    print(f"sum is : {sum}")
        
array_1 = [1, 0, 1, 0]
array_2 = [1, 1, 0, 0]
        
add_binary(array_1, array_2, 4)
    