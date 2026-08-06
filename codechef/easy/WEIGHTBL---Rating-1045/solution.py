T = int(input())
for _ in range(T):
    w1, w2, x1, x2, M = map(int, input().split())
    diff = w2 - w1
    min_gain = x1 * M
    max_gain = x2 * M
    if min_gain <= diff <= max_gain:
        print(1)
    else:
        print(0)