T = int(input())
for _ in range(T):
    A, B, A1, B1, A2, B2 = map(int, input().split())
    
    req = {A, B}
    lang1 = {A1, B1}
    lang2 = {A2, B2}
    
    if req == lang1:
        print(1)
    elif req == lang2:
        print(2)
    else:
        print(0)