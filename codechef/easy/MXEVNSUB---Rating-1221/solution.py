T = int(input())
for i in range(T):
    N = int(input())
    total_sum = (N * (N + 1)) // 2
    if total_sum % 2 == 0:
        print(N)
    else:
        print(N - 1)