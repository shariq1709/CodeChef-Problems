# cook your dish here
import math
T=int(input())
for i in range(T):
    X1,Y1,X2,Y2=map(int,input().split())
    if (Y2-Y1)//(X2-X1)==0:
        print(-1)
    else:
        print(abs((Y2-Y1)//(X2-X1)))