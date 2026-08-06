# CSTOCK - Rating 1045

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-06T14:36:15.521Z  

```py
T = int(input())
for _ in range(T):
    w1, w2, x1, x2, M = map(int, input().split())
    diff = w2 - w1
    min_gain = x1 * M
    max_gain = x2 * M
    if min_gain <= diff <= max_gain:
        print(1)
    else:
        print(0)
```

---

[View on CodeChef](https://www.codechef.com/problems/CSTOCK)