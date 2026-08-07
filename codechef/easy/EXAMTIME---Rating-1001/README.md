# EXAMTIME - Rating 1001

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-07T06:34:41.822Z  

```py
# cook your dish here
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    result=[]
    for i in arr:
        if K>=i:
            result.append("1")
            K=K-i
        else:
            result.append("0")
    print("".join(result))
            
```

---

[View on CodeChef](https://www.codechef.com/problems/EXAMTIME)