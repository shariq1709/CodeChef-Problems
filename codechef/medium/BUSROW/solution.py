# cook your dish here
T=int(input())
for i in range(T):
    N,M,X=map(int,input().split())
    r=(X-1)//M+1
    ans=min(r,N-r+1)
    print(ans)