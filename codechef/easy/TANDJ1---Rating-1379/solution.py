T = int(input())
for _ in range(T):
    a, b, c, d, K = map(int, input().split())
    dist = abs(a - c) + abs(b - d)
    if K >= dist and (K - dist) % 2 == 0:
        print("YES")
    else:
        print("NO")