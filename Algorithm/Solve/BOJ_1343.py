mino = input().split('.')

for i in range(len(mino)):
    if len(mino[i]) == 0:
        continue
    tmp = ''
    while True:
        if len(mino[i]) <= 1:
            tmp += mino[i]
            break
        if len(mino[i]) >= 4:
            tmp += 'AAAA'
            mino[i] = mino[i][4:]
        elif len(mino[i]) >= 2:
            tmp += 'BB'
            mino[i] = mino[i][2:]
    if 'X' in tmp:
        break
    else:
        mino[i] = tmp
    
result = '.'.join(mino)
if 'X' in result:
    print(-1)
else:
    print(result) 