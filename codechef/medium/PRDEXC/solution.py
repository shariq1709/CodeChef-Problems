# cook your dish here
T=int(input())
for i in range(T):
    X,Y,P=map(int,input().split())
    if X*Y>=P:
        print(0)
    else:
        for i in range(1,P+1):
            if (X+i)*Y>=P or (X)*(Y+i)>=P:
                print(i)
                break