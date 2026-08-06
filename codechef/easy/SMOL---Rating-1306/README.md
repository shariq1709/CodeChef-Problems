# SMOL - Rating 1306

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Smallest Possible Whole Number

You are given two integers $N$ and $K$. You may perform the following operation any number of times (including zero): change $N$ to $N-K$, i.e. subtract $K$ from $N$. Find the smallest non-negative integer value of $N$ you can obtain this way.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $K$.
### Output

For each test case, print a single line containing one integer — the smallest value you can get.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^9$
- $0 \leq K \leq 10^9$
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
3
5 2
4 4
2 5
```

```
1
0
2
```

### Explanation:

 **Example case 1:** 

- First, we change $N = 5$ to $N - K = 5 - 2 = 3$.
- Then, we have $N = 3$ and we change it to $N - K = 3 - 2 = 1$.

Since $1 \lt K$, the process stops here and the smallest value is $1$.

 **Example case 2:**  We change $N = 4$ to $N - K = 4 - 4 = 0$. Since $0 \lt K$, the process stops here and the smallest value is $0$.

 **Example case 3:**  Since $2 \lt K$ initially, we should not perform any operations and the smallest value is $2$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-06T14:31:20.724Z  

```py
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    if K == 0:
        print(N)
    else:
        print(N % K)
```

---

[View on CodeChef](https://www.codechef.com/problems/SMOL)