t = int(input())
for _ in range(t):
    d_dsa, d_toc, d_dm = map(int, input().split())
    s_dsa, s_toc, s_dm = map(int, input().split())
    
    dragon_stats = (d_dsa + d_toc + d_dm, d_dsa, d_toc)
    sloth_stats = (s_dsa + s_toc + s_dm, s_dsa, s_toc)
    
    if dragon_stats > sloth_stats:
        print("Dragon")
    elif dragon_stats < sloth_stats:
        print("Sloth")
    else:
        print("Tie")