# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    max_bal = 0
    pos_sum = 0
    
    for j in range(1, N):
        current_bal = arr[j] - j + pos_sum
        
        if current_bal > max_bal:
            max_bal = current_bal
        if arr[j] > 0:
            pos_sum += arr[j]
            
    print(max_bal)