# cook your dish here
# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read A, B, and C for each test case
    a, b, c = map(int, input().split())
    
    # Check if (A + B) / 2 > C
    # This is equivalent to (A + B) > 2 * C
    if (a + b) > (2 * c):
        print("YES")
    else:
        print("NO")# cook your dish here
