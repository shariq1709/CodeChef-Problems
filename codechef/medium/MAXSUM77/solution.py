# cook your dish here
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    new=sorted(arr)
    new[::-1]
    for i in range(1,K+1):
        new.pop()
    print(sum(new))