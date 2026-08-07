# cook your dish here
vowels = {'a', 'e', 'i', 'o', 'u'}
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    consonant_count = 0
    is_hard = False
    
    for char in s:
        if char in vowels:
            consonant_count = 0
        else:
            consonant_count += 1
            if consonant_count >= 4:
                is_hard = True
                break
    
    if is_hard:
        print("NO")
    else:
        print("YES")