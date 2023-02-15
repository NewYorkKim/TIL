n = int(input())
start = 666
tmp = []

while True:
    if '666' in str(start):
        tmp.append(start)
    start += 1
    if len(tmp) == n:
        break

print(tmp[-1])