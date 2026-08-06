# cook your dish here
T=int(input())
for i in range(T):
    A,B,X=map(int,input().split())
    result=(B-A)//X
    print(result)