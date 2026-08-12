# cook your dish here
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    B=set(A)
    len_set=len(B)
    len_arr=len(A)
    if len_set==len_arr:
        print(0)
    else:
        for i in range(0,len(A)+1):
            count=0
            if A[i]==A[i+1]:
                A[i+1]=A[i+1]+1
                count=count+1
        print(count)
        