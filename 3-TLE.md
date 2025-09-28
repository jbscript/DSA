## What is TLE?

**TLE** stands for **Time Limit Exceeded**.
It means your solution **did not finish running within the allowed time** defined by the problem. Once your program exceeds the limit (usually 1–2 seconds per test case), LeetCode stops execution and reports **TLE**.

---

## Why Does TLE Happen?

Common reasons:

| Cause                 | Example                             |
| --------------------- | ----------------------------------- |
| Inefficient algorithm | Using **O(n²)** when `n = 10⁵`      |
| Too many nested loops | Double/triple loops on large arrays |
| Repeated calculations | Not using caching or memoization    |
| I/O inside loops      | Printing or reading repeatedly      |

---

## Choosing the Right Time Complexity

Before coding, **check the constraints**.
Your approach must match the input size:

| Input Size (n) | Recommended Time Complexity             |
| -------------- | --------------------------------------- |
| ≤ 100          | ✅ O(n²) or even O(n³)                  |
| ≤ 10⁴          | ⚠ O(n²) is borderline                   |
| ≤ 10⁵ – 10⁶    | ✅ O(n) / O(n log n) only               |
| > 10⁷          | ✅ Needs optimized math / constant time |

---

## Example

If a problem says:

```
Constraints: 1 <= n <= 10^5
```

Avoid:

```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        // O(n²) → 10¹⁰ operations → TLE
    }
}
```

Use **O(n)** or **O(n log n)** instead (e.g., prefix sums, hash maps, sorting-based logic, etc.).

---

## Summary

✔ TLE means **your code is too slow**.
✔ Always **analyze constraints before coding**.
✔ Choose **algorithms that match input size**.

---
