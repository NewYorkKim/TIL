t = int(input())

for i in range(1, t+1):
    target = input()
    start = '0' * len(target)

    cnt = 0
    for j in range(len(target)):
        if target == start:
            break
        if target[j] == start[j]:
            continue
        else:
            if start[j] == '1':
                start = start[:j] + start[j:].replace('1', '0')
                cnt += 1
            else:
                start = start[:j] + start[j:].replace('0', '1')
                cnt += 1

    print(f"#{i}", cnt)