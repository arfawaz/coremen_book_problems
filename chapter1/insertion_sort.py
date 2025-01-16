#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:47:54 2025

@author: fawaz
"""

'''
In the original insertion example given in text the parameter n is passed into
the fucntion as well. But here for simplicity of testing the correctness of the 
algorithm without having the count the number of elements in the array each
time I am taking a short cut. The steps required to calculate the length of the
array by the line len(array) cannot be counted into the algorithm.
'''

def insertionSort(array):
    print(f"Original Array is:{array}")
    n = len(array)
    for i in range(1,n):
        for j in range(i):
            if array[i-j] < array[i-j-1]:
                temp = array[i-j-1]
                array[i-j-1] = array[i-j]
                array[i-j] = temp
            else:
                break
    print(f"Sorted array is: {array}")
            

array = [5,2,4,6,1,3]

insertionSort(array)