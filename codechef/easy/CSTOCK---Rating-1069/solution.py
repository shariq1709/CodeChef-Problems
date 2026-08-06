# cook your dish here
T=int(input())
for i in range(T):
    S,A,B,C=map(int,input().split())
    price_of_stock=S*(1+(C/100))
    if price_of_stock>=A and price_of_stock<=B:
        print("Yes")
    else:
        print("No")