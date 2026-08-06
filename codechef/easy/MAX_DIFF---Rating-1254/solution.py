# cook your dish here
T=int(input())
for i in range(T):
    N,S=map(int,input().split())
    if S<=N:
        print(S)
    else:
        print(2*N-S)