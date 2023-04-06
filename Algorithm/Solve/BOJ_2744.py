s = input()
result = ''

for i in s:
    if i.islower():
        result += i.upper()
    else:
        result += i.lower()

print(result)