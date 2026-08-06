T = int(input())
for i in range(T):
    U, V, A, S = map(int, input().split())
    v_squared = U**2 - 2 * A * S
    if v_squared <= V**2:
        print("Yes")
    else:
        print("No")