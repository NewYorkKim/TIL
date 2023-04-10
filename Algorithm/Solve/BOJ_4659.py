vowels = ['a', 'e', 'i', 'o', 'u']
allows = ['e', 'o']

while True:
    case = input()
    if case == "end":
        break
    flag = False
    cnt1, cnt2 = 0, 0
    result = True
    for i in range(len(case)):
        if case[i] in vowels:
            flag = True
            cnt1 += 1
            cnt2 = 0
        else:
            cnt1 = 0
            cnt2 += 1
        if (cnt1 >= 3) or (cnt2 >= 3):
            result = False
            break
        if (i > 0) and (case[i] not in allows) and (case[i-1] == case[i]):
            result = False
            break
    if result and flag:
        print(f"<{case}> is acceptable.")
    else:
        print(f"<{case}> is not acceptable.")