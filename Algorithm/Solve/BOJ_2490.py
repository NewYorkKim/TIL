for _ in range(3):
    bars = sum(list(map(int, input().split())))

    if bars == 0:
        print("D")
    elif bars == 1:
        print("C")
    elif bars == 2:
        print("B")
    elif bars == 3:
        print("A")
    elif bars == 4:
        print("E")
