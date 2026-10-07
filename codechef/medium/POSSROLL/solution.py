# cook your dish here
X,K,Y=map(int,input().split())
new_list=[]
for i in range(1,X+1):
    new_list.append(i*K)
if Y in new_list:
    print("YES")
else:
    print("NO")