# cook your dish here
import math
T=int(input())
for i in range(T):
    N=int(input())
    if N==1:
        print(1)
    else:
        print(math.ceil(N/2))