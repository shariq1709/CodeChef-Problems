# ENCMSG - Rating 1027

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Encoding Message

Chef recently graduated Computer Science in university, so he was looking for a job. He applied for several job offers, but he eventually settled for a software engineering job at ShareChat. Chef was very enthusiastic about his new job and the first mission assigned to him was to implement a message encoding feature to ensure the chat is private and secure.

Chef has a message, which is a string $S$ with length $N$ containing only lowercase English letters. It should be encoded in two steps as follows:

- Swap the first and second character of the string $S$, then swap the 3rd and 4th character, then the 5th and 6th character and so on. If the length of $S$ is odd, the last character should not be swapped with any other.
- Replace each occurrence of the letter 'a' in the message obtained after the first step by the letter 'z', each occurrence of 'b' by 'y', each occurrence of 'c' by 'x', etc, and each occurrence of 'z' in the message obtained after the first step by 'a'.

The string produced in the second step is the encoded message. Help Chef and find this message.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains the message string $S$.
### Output

For each test case, print a single line containing one string — the encoded message.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N \le 100$
- $|S| = N$
- $S$ contains only lowercase English letters
### Sample 1:
Input
Output

```
2
9
sharechat
4
chef

```

```
shizxvzsg
sxuv
```

### Explanation:

 **Example case 1:**  The original message is "sharechat". In the first step, we swap four pairs of letters (note that the last letter is not swapped), so it becomes "hsraceaht". In the second step, we replace the first letter ('h') by 's', the second letter ('s') by 'h', and so on, so the resulting encoded message is "shizxvzsg".

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-08T13:50:42.084Z  

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

[View on CodeChef](https://www.codechef.com/problems/ENCMSG)