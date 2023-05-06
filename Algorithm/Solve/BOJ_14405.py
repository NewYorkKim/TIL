s = input()
s = s.replace('pi', ' ').replace('ka', ' ').replace('chu', ' ')

if s.strip() == '':
    print('YES')
else:
    print('NO')