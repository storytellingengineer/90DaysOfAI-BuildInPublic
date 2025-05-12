# 🧮 Bubble Sort Algorithm

Bubble Sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order. It gets its name because smaller elements "bubble" to the top (beginning) of the list.

---

## 🔍 How It Works

1. Start at the beginning of the list.
2. Compare the current element with the next one.
3. If the current element is greater, swap them.
4. Move to the next pair and repeat.
5. After each full pass, the largest element gets placed at the end.
6. Repeat the process for the remaining unsorted portion.

---
## 📊 Time and Space Complexity

| Case    | Time Complexity |
|---------|------------------|
| Best    | O(n)             |
| Average | O(n²)            |
| Worst   | O(n²)            |

- **Space Complexity**: O(1) (in-place sorting)

---

## 💡 When to Use

- For educational purposes to demonstrate basic sorting logic  
- Small datasets where performance is not critical

---

## ⚠️ Limitations

- Not suitable for large datasets  
- Inefficient compared to other sorting algorithms like Merge Sort or Quick Sort

---

## 🧠 Interview Tip

Although Bubble Sort is rarely used in real applications, interviewers may ask you to write it to test your understanding of loops, conditionals, and swapping logic.
