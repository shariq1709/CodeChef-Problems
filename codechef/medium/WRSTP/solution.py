# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    S=input()
    x=0
    y=0
    new_list=list(S)
    for i in new_list:
        if i=='U':
            y=y+1
        elif i=='D':
            y=y-1
        elif i=='L':
            x=x-1
        else:
            x=x+1
    