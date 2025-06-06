# -*- coding: utf-8 -*-
"""jump_search.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xHLB1d8yus5BJsQJ0RBgJyebT1KjQD0B
"""

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size
    prev = 0

    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 13, 18, 21]
target = 13
result = jump_search(arr, target)
print("Element found at index:", result)

