# LPYAS140

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Develop a function to compute and return the area of a rectangle, given its length and width

### Sample 1:
Input
Output

```
5 8
```

```
40
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-29T06:12:25.197Z  

```py
def calculate_area(length, width):
    # Write your code here
    result=length*width
    return result
    
def main():
    length, width = map(int, input().split())
    area = calculate_area(length, width)
    print(area)


main()

```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS140)