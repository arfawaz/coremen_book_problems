#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:00:16 2025

@author: fawaz
"""


def insertionSortDecreasing(array):
    print(f"Original Array is:{array}")
    n = len(array)
    for i in range(1,n):
        for j in range(i):
            if array[i-j] > array[i-j-1]:
                temp = array[i-j-1]
                array[i-j-1] = array[i-j]
                array[i-j] = temp
            else:
                break
    print(f"Sorted in decreasing order array is: {array}")
            

array = [5,2,4,6,1,3]

insertionSortDecreasing(array)