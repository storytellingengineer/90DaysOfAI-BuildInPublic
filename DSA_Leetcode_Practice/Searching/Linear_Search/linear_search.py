# -*- coding: utf-8 -*-
"""linear_search.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xHLB1d8yus5BJsQJ0RBgJyebT1KjQD0B
"""

def linear_search(arr, target):
    """
    Linear Search Algorithm
    Returns index of target if found, else -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    target = 70
    result = linear_search(arr, target)
    print(f"Element found at index: {result}" if result != -1 else "Element not found")

