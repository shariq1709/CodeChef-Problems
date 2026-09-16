# cook your dish here
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    if K == N - 1:
        print("No")
    else:
        print("Yes")