s = input()
k = input()

s_string = ''.join([i for i in s if not i.isdecimal()])

if k in s_string:
    print(1)
else:
    print(0)