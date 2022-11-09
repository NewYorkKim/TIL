i = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    div, mod = divmod(v, p)
    if mod > l:
        mod = l
    print(f'Case {i}: {div*l + mod}')
    i += 1
