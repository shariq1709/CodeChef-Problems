# cook your dish here
T=int(input())
for i in range(T):
    N,X,Y=map(int,input().split())
    total=(3*X)+((N-3)*Y)
    if N>=3:
        print(N*X)
    else:
        print(total)