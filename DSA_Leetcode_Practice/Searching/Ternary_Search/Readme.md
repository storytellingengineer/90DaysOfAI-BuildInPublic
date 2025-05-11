# Ternary Search

Ternary Search is an efficient algorithm to search for an element in a **sorted array** by dividing the array into three parts instead of two (like binary search). It recursively narrows down the search space based on comparisons, making it efficient for large data sets.

---

## 📌 How It Works

1. **Divide the array into 3 parts:**
   - The array is divided into three parts by selecting two midpoints `mid1` and `mid2`.
2. **Compare the target with mid1 and mid2:**
   - If the target matches `mid1`, return `mid1`.
   - If the target matches `mid2`, return `mid2`.
3. **Narrow down the search range:**
   - If the target is smaller than `mid1`, search the left part.
   - If the target is larger than `mid2`, search the right part.
   - Otherwise, search between `mid1` and `mid2`.

---

## ✅ Use Case

- Suitable for **sorted arrays**.
- Works best when dividing the search space into three parts offers a performance advantage over binary search.
- Example: Searching for values in sorted data (like price range, timestamps, etc.).

---

## 🧠 Time & Space Complexity

| Case       | Time Complexity      |
|------------|----------------------|
| Best       | O(1)                 |
| Average    | O(log₃ n)            |
| Worst      | O(log₃ n)            |

- **Space Complexity:** O(log₃ n) due to recursion (for the stack)


## ⚠️ Limitations
- Not ideal for unsorted data.
- Recursive implementation may have performance drawbacks on very large arrays due to stack depth limitations.


## **Explanation:**

1. **Time Complexity:**
   - The ternary search divides the search space into 3 parts instead of 2, but it still has a logarithmic time complexity. Each recursive call reduces the search space by about one-third, so the time complexity is `O(log₃ n)`.

2. **Space Complexity:**
   - Due to the recursive calls, the space complexity is also logarithmic in nature, `O(log₃ n)`.
