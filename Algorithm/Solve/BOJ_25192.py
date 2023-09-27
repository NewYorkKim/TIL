n = int(input())

cnt = 0
previous = set()
for _ in range(n):
    chat = input()

    if chat == "ENTER":
        cnt += len(previous)
        previous = set()
        continue

    previous.add(chat)

cnt += len(previous)
print(cnt)