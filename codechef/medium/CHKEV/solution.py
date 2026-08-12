# cook your dish here
L,R=map(int,input().split())
flag=0
for i in range(L,R+1):
    if i%2==0:
        flag=1
        break
if flag==1:
    print("Yes")
else:
    print("No")