s = input()
cnt = [0] * 26

for i in s:
    idx = ord(i) - 97
    cnt[idx] += 1

print(*cnt)