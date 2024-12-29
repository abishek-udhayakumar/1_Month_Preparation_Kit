#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0

    # Iterate over the array to count positive, negative, and zero values
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    arr_count = len(arr)

    # Calculate fractions
    positive_fraction = positive_count / arr_count
    negative_fraction = negative_count / arr_count
    zero_fraction = zero_count / arr_count

    # Print fractions formatted to 6 decimal places
    print(f"{positive_fraction:.6f}")
    print(f"{negative_fraction:.6f}")
    print(f"{zero_fraction:.6f}")

if __name__ == '__main__':
    n = int(input().strip())  # Read the size of the array
    arr = list(map(int, input().rstrip().split()))  # Read the array elements

    plusMinus(arr)
