t = int(input())
vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(1, t+1):
    word = input()
    result = ''
    
    for c in word:
        if c in vowels:
            continue
        else:
            result += c
    
    print(f"#{i}", result)