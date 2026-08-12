# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    R = sum(1 for x in A if x % 2 != 0)
    if S % 2 == 0:
        print(S - (R // 2))
    else:
        print((R - 1) // 2)
    