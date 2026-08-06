# cook your dish here
T=int(input())
for i in range(T):
    D,L,R=map(int,input().split())
    if D>=L and D<=R:
        print("Take second dose now")
    elif D>L and D>R:
        print("Too Late")
    elif D<L and D<R:
        print("Too Early")
    else:
        print("Take second dose now")