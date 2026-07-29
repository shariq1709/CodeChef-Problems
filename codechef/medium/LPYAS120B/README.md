# LPYAS120B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program to calculate the sum of first  **N**  multiples of 3 and print it.

Check the sample input / output below for further clarity.

### Input Format
- The only input is an integer N.
### Output Format
- The only output is the sum of first N multiples of 3.
### Sample 1:
Input
Output

```
4
```

```
30
```

### Explanation:

First 4 multiples of 3 are: 3, 6, 9 and 12
Hence, 3 + 6 + 9 + 12 = 30

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-29T06:22:45.845Z  

```py
N = int(input())
# Updae the code below this line
sum_=0
for i in range(1,N+1):
    sum_=sum_+3*i
print(sum_)
    
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS120B)