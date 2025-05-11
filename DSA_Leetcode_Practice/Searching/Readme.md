# 🔍 Searching Algorithms in Python

This folder contains Python implementations and explanations for various **searching algorithms** — fundamental tools used to locate data within a structure like an array or list.

---

## 📦 Included Algorithms

| Algorithm         | Description                                                                 | Best Use Case                                         | Time Complexity (Best/Average/Worst) | Space Complexity |
|------------------|------------------------------------------------------------------------------|-------------------------------------------------------|---------------------------------------|------------------|
| **Linear Search** | Sequentially checks each element until match is found                       | Unsorted or small datasets                           | O(1) / O(n) / O(n)                    | O(1)             |
| **Binary Search** | Repeatedly divides sorted array to find target                              | Sorted arrays                                        | O(1) / O(log n) / O(log n)           | O(1)             |
| **Jump Search**   | Jumps ahead by fixed steps, then linearly searches block                    | Large sorted arrays                                  | O(1) / O(√n) / O(√n)                 | O(1)             |
| **Interpolation Search** | Estimates target position in sorted uniform dataset             | Uniformly distributed sorted arrays                  | O(1) / O(log log n) / O(n)           | O(1)             |
| **Exponential Search** | Combines binary search with exponential jumps                          | Unbounded/infinite-size sorted arrays                | O(log i), where i = index of target  | O(1)             |
| **Ternary Search**| Divides the array into 3 parts instead of 2                                 | Sorted arrays, when mid-point split is optimal       | O(log₃ n)                            | O(1)             |

---

## 📌 What is a Searching Algorithm?

Searching algorithms help find the position of a specific element in a data structure (like a list or array). The choice of algorithm depends on factors like:
- Whether the array is sorted
- Size of the dataset
- Expected frequency or distribution of elements
- Memory constraints

---

## 🧠 How to Choose the Right Algorithm

- Use **Linear Search** for small or unsorted datasets.
- Use **Binary Search** when working with sorted data for fast performance.
- Use **Jump Search** or **Interpolation Search** for large, sorted datasets where indexing patterns help.
- Use **Exponential Search** when you're unsure of array size (e.g., online data streams).
- Use **Ternary Search** for optimization problems or when splitting in thirds is preferable.
