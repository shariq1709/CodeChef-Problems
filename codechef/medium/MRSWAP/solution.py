t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max_sum = 0
    for i in range(n):
        max_sum += max(arr[i], arr[2 * n - 1 - i])
    print(max_sum)