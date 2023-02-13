for i in range(10):
    n, password = input().split()

    while True:
        fix = 0
        password2 = password
        for j in range(len(password)-1):
            if password[j] == password[j+1]:
                password2 = password[:j] + password[j+2:]
                fix += 1
        password = password2
        if fix == 0:
            break

    print(f"#{i+1}", password)
