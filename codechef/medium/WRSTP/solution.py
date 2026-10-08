# cook your dish here
# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    
    x = 0
    y = 0
    new_list = list(S)
    
    # Calculate the initial total displacement
    for i in new_list:
        if i == 'U':
            y = y + 1
        elif i == 'D':
            y = y - 1
        elif i == 'L':
            x = x - 1
        else:
            x = x + 1
            
    possible = False

    for i in new_list:
        curr_x, curr_y = x, y
        
        # Undo the effect of the current move and apply its opposite
        if i == 'U':
            curr_y = curr_y - 2
        elif i == 'D':
            curr_y = curr_y + 2
        elif i == 'L':
            curr_x = curr_x + 2
        else:
            curr_x = curr_x - 2
            
        if curr_x == 0 and curr_y == 0:
            possible = True
            break
            
    if possible:
        print("YES")
    else:
        print("NO")