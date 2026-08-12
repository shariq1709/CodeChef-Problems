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
        A.sort()
        max_d=0
        sum_d=0
        for i in range(1,len(A)):
            if A[i]<=A[i-1]:
                d=A[i-1]+1-A[i]
                A[i]=A[i-1]+1
                sum_d=sum_d+d
                if d>max_d:
                    max_d=d
        count=max(max_d,(sum_d+K-1)//K)
        print(count)