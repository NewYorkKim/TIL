t = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(t):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    if int(month) < 1 or int(month) > 12:
        result = -1
    else:
        if int(day) < 1 or int(day) > int(days[int(month)-1]):
            result = -1
        else:
            result = '/'.join([year, month, day])

    print(result)
         