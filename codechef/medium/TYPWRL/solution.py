# cook your dish here
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    S = input()
    L = input()
    
    new_list = list(S)
    new_list2 = list(L)
    
    max_ = 0
    current_streak = 0
    last_hand = None
    
    for i in new_list:
        if i in new_list2:
            hand = 'left'
        else:
            hand = 'right'
            
        if hand == last_hand:
            current_streak += 1
        else:
            current_streak = 1
            last_hand = hand
            
        if current_streak > max_:
            max_ = current_streak
            
    print(max_)