s = input()

tag = False
result = ''
tmp = ''

for i in range(len(s)):
    if s[i] == '<':
        result += tmp[::-1]
        tmp = s[i]
        tag = True
    elif s[i] == '>':
        tmp += s[i]
        result += tmp
        tag = False
        tmp = ''
    elif (tag == False) & (s[i] == ' '):
        result += tmp[::-1] + ' '
        tmp = ''
    else:
        tmp += s[i]
        if i == len(s) - 1:
            result += tmp[::-1]

print(result)