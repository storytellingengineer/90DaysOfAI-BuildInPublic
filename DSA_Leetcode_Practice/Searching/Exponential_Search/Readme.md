# 📍 Exponential Search

Exponential Search (also known as **Exponential Binary Search**) is a search algorithm that works efficiently on **sorted arrays**. It first checks for the element at the first index and then **exponentially increases** the range by doubling the search index until it finds an index with a value greater than or equal to the target. Once the range is found, it uses **binary search** on that range.

---

## 📌 How It Works

1. **First, check if the element is at the first index.**
2. **Exponentially increase the range.**
   - Start at index 1, then check 2, 4, 8, 16, and so on until you reach an element greater than or equal to the target.
3. **Apply Binary Search** on the range determined by exponential growth.

---

## ✅ Use Case

- Works well on **sorted arrays** when you don’t know the size of the array in advance.
- More efficient than linear search but useful in **large data sets**.
- Example: Searching for a large range of values in a database without pre-indexing.

---

## 🧠 Time & Space Complexity

| Case       | Time Complexity      |
|------------|----------------------|
| Best       | O(1)                 |
| Average    | O(log n)             |
| Worst      | O(log n)             |

- **Space Complexity:** O(1) — iterative approach

---

## ⚠️ Limitations
- Not suitable for unsorted arrays.
- Performance can degrade if the data distribution is skewed.

- ---

### **Explanation:**

1. **Time Complexity:**
   - The exponential search can eliminate half of the search space after each exponential step. 
   - In the worst case, it performs `O(log n)` operations to find the range, and then it performs a `binary search` over that range, which is `O(log n)`.

2. **Space Complexity:**
   - This algorithm only requires a few extra variables to keep track of the range, making it space-efficient with `O(1)` space complexity.

---
