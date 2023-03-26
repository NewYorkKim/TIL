stroke = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

string = input()
cnt = [stroke[ord(s)-65] for s in string]

while len(cnt) != 1:
    tmp = []
    for i in range(0, len(cnt), 2):
        if i == len(cnt) - 1:
            tmp.append(cnt[i])
        else:
            tmp.append(cnt[i] + cnt[i+1])
    cnt = tmp

if cnt[0] % 2 != 0:
    print("I'm a winner!")
else:
    print("You're the winner?") 