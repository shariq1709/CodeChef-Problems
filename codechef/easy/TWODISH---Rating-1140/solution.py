T = int(input())
for _ in range(T):
    N, A, B, C = map(int, input().split())
    if min(B, A + C) >= N:
        print("YES")
    else:
        print("NO")