# cook your dish here
T=int(input())
for i in range(T):
    X,Y,P=map(int,input().split())
    if X*Y>=10:
        print(0)
    else:
        for i in range(1,P+1):
            if (X+i)*Y>=10 or (X)*(Y-i)>=10:
                print(i)
                break