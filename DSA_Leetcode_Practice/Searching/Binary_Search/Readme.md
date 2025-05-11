# 🔍 Binary Search

Binary Search is one of the most efficient searching algorithms used on **sorted** arrays. It repeatedly divides the search interval in half to find the target.

---

## ✅ How It Works

1. Find the middle element of the array.
2. If it matches the target, return the index.
3. If the target is smaller, repeat the search on the left half.
4. If the target is greater, repeat the search on the right half.
5. Repeat until the element is found or the interval is empty.

---

## 📈 Time & Space Complexity

| Complexity       | Value           |
|------------------|-----------------|
| Best Case        | O(1)            |
| Average Case     | O(log n)        |
| Worst Case       | O(log n)        |
| Space Complexity | O(1) (iterative) |

---

## 🧠 When to Use

- When the array is sorted.
- When speed is critical for large datasets.
- Very efficient for datasets that are not changing often.
