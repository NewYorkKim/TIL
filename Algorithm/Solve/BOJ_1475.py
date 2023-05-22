nums = input()
room = [0] * 10
cnt = 1

for num in nums:
    num = int(num)
    if (num == 6) or (num == 9):
        if room[num] == 0:
            room[num] += 1