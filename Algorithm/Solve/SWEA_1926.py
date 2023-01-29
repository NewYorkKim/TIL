# import re

# n = int(input())
# for i in range(1, n+1):
#     i = re.sub("[369]", "-", str(i))
#     if '-' in i:
#         i = re.sub("[0-9]", "", i)
#     print(i, end=" ")

n = int(input())

for i in range(1, n+1):
    trans = str(i).maketrans("369", "---")
    i = str(i).translate(trans)
    if '-' in i:
        trans = i.maketrans("", "", "0123456789")
        i = i.translate(trans)
    print(i, end=" ")
