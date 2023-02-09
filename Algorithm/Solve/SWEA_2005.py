t = int(input())

for i in range(1, t+1):
    n = int(input())
    print(f"#{i}")
    for j in range(n):
        for k in range(j+1):
            if (k == 0) | (k == j):
                print(1, end=" ")
            else:
                print(j, end=" ")
        print()
  