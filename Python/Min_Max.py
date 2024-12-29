#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Initialize variables
    total_sum = 0
    min_value = float('inf')
    max_value = -float('inf')
    

    for num in arr:
        total_sum += num
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    
    
    min_sum = total_sum - max_value
    max_sum = total_sum - min_value
    
    # Print the result
    print(min_sum, max_sum)
            
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
