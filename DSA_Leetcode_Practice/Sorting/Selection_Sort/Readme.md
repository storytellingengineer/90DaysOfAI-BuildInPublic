# 📘 Selection Sort

Selection Sort is a simple comparison-based sorting algorithm. It repeatedly selects the minimum element from the unsorted portion and places it at the beginning of the sorted portion.

---

## 🔍 How It Works

1. Start from the beginning of the array.
2. Find the minimum element in the unsorted part.
3. Swap it with the first unsorted element.
4. Repeat until the array is sorted.

---

## 📊 Time and Space Complexity

| Case     | Time Complexity |
|----------|-----------------|
| Best     | O(n²)           |
| Average  | O(n²)           |
| Worst    | O(n²)           |

**Space Complexity**: O(1) – In-place sorting (no extra space used)

---

## 💡 When to Use
- Suitable for small datasets
- Easy to implement and understand
- Useful when memory space is limited (since it's in-place)

## ⚠️ Limitations
- Inefficient on large datasets
- Performs poorly compared to advanced algorithms like Merge Sort or Quick Sort

## 🧠 Interview Tip
- Selection Sort is often asked to:
- Test your understanding of nested loops, indexing, and element swapping
- Compare performance and approach with Bubble Sort or Insertion Sort
