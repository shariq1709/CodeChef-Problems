T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    max_rating = 0
    for _ in range(N):
        S, R = map(int, input().split())
        if S <= X:
            max_rating = max(max_rating, R)
    print(max_rating)