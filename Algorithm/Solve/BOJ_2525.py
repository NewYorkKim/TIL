# hour, minute = map(int, input().split())
# taking = int(input())

# if minute + taking >= 60:
#     get_hour = hour + (minute + taking)  // 60
#     get_minute = (minute + taking) % 60
#     if get_hour > 23:
#         get_hour = get_hour % 24
# else:
#     get_hour = hour
#     get_minute = minute + taking

# print(get_hour, get_minute)

hour, minute = map(int, input().split())
taking = int(input())

get_minute = (minute + taking) % 60
get_hour = ((minute + taking) // 60 + hour) % 24

print(get_hour, get_minute)