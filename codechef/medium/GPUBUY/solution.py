# cook your dish here
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    if Z<=Y:
        print(-1)
    else:
        print((X+(Z-Y)-1)//(Z-Y))