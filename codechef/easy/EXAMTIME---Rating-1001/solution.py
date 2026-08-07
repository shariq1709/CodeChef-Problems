# cook your dish here
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    arr=list(map(int,input().split()))
    result=[]
    for i in arr:
        if K>=i:
            result.append("1")
            K=K-i
        else:
            result.append("0")
    print("".join(result))
            