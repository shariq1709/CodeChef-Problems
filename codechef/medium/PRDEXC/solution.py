import math

T = int(input())
for _ in range(T):
    X, Y, P = map(int, input().split())
    if X * Y >= P:
        print(0)
    else:
       
        for k in range(1, 201):
            if any((X + a) * (Y + (k - a)) >= P for a in range(k + 1)):
                print(k)
                break