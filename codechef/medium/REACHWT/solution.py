T = int(input())
for _ in range(T):
    N = int(input())
    if N % 2 == 0:
        print((N // 2) * 30)
    else:
        print(((N // 2) * 30) + 20)