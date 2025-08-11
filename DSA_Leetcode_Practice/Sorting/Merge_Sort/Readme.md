# Merge Sort in Python

## 📌 Overview
This repository contains a simple and clean implementation of the **Merge Sort** algorithm in Python.  
Merge Sort is a **divide-and-conquer** algorithm that:
1. Splits the array into two halves.
2. Recursively sorts each half.
3. Merges the sorted halves into a single sorted array.

It has:
- **Time Complexity:** `O(n log n)` in all cases (Best, Average, Worst)
- **Space Complexity:** `O(n)` due to extra space for merging.

---

## 🚀 How It Works
1. **Divide** – The list is divided into two halves until each sublist has one element.
2. **Conquer** – Each sublist is sorted recursively.
3. **Combine** – The sorted sublists are merged to form the final sorted list.

---

## 📝 Code Example
```python
from merge_sort import merge_sort

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
```

```
Original array: [38, 27, 43, 3, 9, 82, 10]
Sorted array: [3, 9, 10, 27, 38, 43, 82]
```

## 🧠 Key Points
- Merge Sort is a stable sorting algorithm.
- Performs well on large datasets.
- Requires additional space for merging.
