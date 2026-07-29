import math

T = int(input())
for _ in range(T):
    X, Y, P = map(int, input().split())
    if X * Y >= P:
        print(0)
    else:
        incX = math.ceil(P / Y) - X
        incY = math.ceil(P / X) - Y
        print(min(incX, incY))
