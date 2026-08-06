T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    if K == 0:
        print(N)
    else:
        print(N % K)