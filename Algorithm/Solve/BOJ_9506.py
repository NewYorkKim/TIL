while True:
    n = int(input())

    if n == -1:
        break

    tmp = []
    for i in range(1, n):
        if n % i == 0:
            tmp.append(i)

    if n == sum(tmp):
        print(f"{n} =", ' + '.join(list(map(str, tmp))))
    else:
        print(f"{n} is NOT perfect.")