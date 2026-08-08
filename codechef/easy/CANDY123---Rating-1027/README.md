# CANDY123 - Rating 1027

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-08T13:50:58.510Z  

```py
T = int(input())
for i in range(T):
    N = int(input())
    S = list(input()) 
    for j in range(0, N - 1, 2):
        S[j], S[j + 1] = S[j + 1], S[j]
    for i in range(len(S)):
        if S[i] == 'a':
            S[i] = 'z'
        elif S[i] == 'b':
            S[i] = 'y'
        elif S[i] == 'c':
            S[i] = 'x'
        elif S[i] == 'd':
            S[i] = 'w'
        elif S[i] == 'e':
            S[i] = 'v'
        elif S[i] == 'f':
            S[i] = 'u'
        elif S[i] == 'g':
            S[i] = 't'
        elif S[i] == 'h':
            S[i] = 's'
        elif S[i] == 'i':
            S[i] = 'r'
        elif S[i] == 'j':
            S[i] = 'q'
        elif S[i] == 'k':
            S[i] = 'p'
        elif S[i] == 'l':
            S[i] = 'o'
        elif S[i] == 'm':
            S[i] = 'n'
        elif S[i] == 'n':
            S[i] = 'm'
        elif S[i] == 'o':
            S[i] = 'l'
        elif S[i] == 'p':
            S[i] = 'k'
        elif S[i] == 'q':
            S[i] = 'j'
        elif S[i] == 'r':
            S[i] = 'i'
        elif S[i] == 's':
            S[i] = 'h'
        elif S[i] == 't':
            S[i] = 'g'
        elif S[i] == 'u':
            S[i] = 'f'
        elif S[i] == 'v':
            S[i] = 'e'
        elif S[i] == 'w':
            S[i] = 'd'
        elif S[i] == 'x':
            S[i] = 'c'
        elif S[i] == 'y':
            S[i] = 'b'
        elif S[i] == 'z':
            S[i] = 'a'

    print("".join(S))
```

---

[View on CodeChef](https://www.codechef.com/problems/CANDY123)