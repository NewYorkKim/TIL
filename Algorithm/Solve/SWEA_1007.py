t = int(input())

for i in range(1, t+1):
    string = input()
    tmp = '' + string[0]
    for j in range(1, len(string)):
        if tmp != string[j:j+len(tmp)]:
            tmp += string[j]
        else:
            break
    print(f"#{i}", len(tmp))
