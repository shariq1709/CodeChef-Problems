# Read the number of test cases
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    
    # If K is less than or equal to N, everyone gets an empty row.
    # Otherwise, K - N people will have to share a row.
    if K <= N:
        print(0)
    else:
        print(K - N)