# Interpolation Search

Interpolation Search is an **improved variant of Binary Search** used specifically for **uniformly distributed sorted arrays**. Instead of always dividing the search space into halves, it **estimates the probable position** of the element based on its value.

---

## 📌 How It Works

It uses the formula:

```
pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])
```
This formula assumes uniform distribution and **interpolates** the likely index where the target might be.

---

## ✅ Use Case

- Arrays where the data is **sorted and uniformly distributed**
- Faster than binary search in such cases
- Examples: Searching in sensor readings, indexes, price ranges

---

## 🧠 Time & Space Complexity

| Case       | Time Complexity     |
|------------|---------------------|
| Best       | O(1)                |
| Average    | O(log log n)        |
| Worst      | O(n)                |

- **Space Complexity:** O(1) — iterative implementation

## ⚠️ Limitations
- Doesn't perform well on non-uniformly distributed data
- Can give incorrect estimates if ```arr[low] == arr[high]```


