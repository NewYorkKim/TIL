for i in range(5):
    for j in range(5):
        if i == j:
            mark = '#'
        else:
            mark = '+'
        print(mark, end='')
    print()