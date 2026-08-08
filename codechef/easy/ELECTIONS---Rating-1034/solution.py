# cook your dish here
T = int(input())
for i in range(T):
    Xa, Xb, Xc = map(int, input().split())
    
    if Xa > 50:
        print("A")
    elif Xb > 50:
        print("B")
    elif Xc > 50:
        print("C")
    else:
        print("NOTA")