# cook your dish here
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    rem_len = n - k
    curr_sum = sum(a[:rem_len])
    max_sum = curr_sum
    for i in range(rem_len, n):
        curr_sum += a[i] - a[i - rem_len]
        max_sum = max(max_sum, curr_sum)
    print(max_sum)