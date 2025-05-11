# 🔍 Jump Search

Jump Search is a searching algorithm for sorted arrays that works by jumping ahead by a fixed number of elements (typically √n), and then performing linear search within the identified block.

---

## ✅ How it Works
1. Choose a jump step of √n (where n is the length of array).
2. Jump ahead in steps until the element at that index is greater than or equal to the target.
3. Perform linear search in the previous block.

---

## 📈 Time & Space Complexity

| Complexity      | Value           |
|----------------|-----------------|
| Best Case       | O(1)            |
| Average Case    | O(√n)           |
| Worst Case      | O(√n)           |
| Space           | O(1)            |

---

## 🧠 When to Use
- When array is sorted.
- You want a faster alternative to linear search but don’t want full binary search logic.
