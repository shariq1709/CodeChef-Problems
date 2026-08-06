# cook your dish here
T=int(input())
for i in range(T):
    x=int(input())
    if 1<=x and x<100:
        print("Easy")
    elif 100<=x and x<200:
        print("Medium")
    else:
        print("Hard")