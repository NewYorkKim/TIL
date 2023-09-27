n = int(input())

flag = False
previous = set()
for _ in range(n):
    a, b = input().split()
    
    if (a == "ChongChong") or (b == "ChongChong"):
        flag = True
        previous.add(a)
        previous.add(b)
        continue
    
    if flag:
        if (a in previous) or (b in previous):
            previous.add(a)
            previous.add(b)

print(len(previous))
