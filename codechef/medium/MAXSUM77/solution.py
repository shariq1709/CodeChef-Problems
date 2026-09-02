# cook your dish here
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # 1. Sort the list in descending order to get largest numbers first
    new = sorted(arr)
    new = new[::-1]  # Note: new[::-1] must be reassigned back to 'new'
    
    # 2. To get the maximum sum after removing K elements from a sorted list,
    # simply drop the K smallest elements (which are now at the end)
    for i in range(1, K + 1):
        new.pop()  # Use pop() to remove elements instead of append()
        
    print(sum(new))