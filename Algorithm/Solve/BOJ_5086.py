while True:
    first, second = map(int, input().split())
    if first == 0 and second == 0:
        break
    if first % second == 0:
        print('multiple')
    elif second % first == 0:
        print('factor')
    else:
        print('neither')