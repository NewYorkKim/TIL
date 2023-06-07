while True:
    sides = sorted(list(map(int, input().split())))
    if sides[0] == sides[1] == sides[2] == 0:
        break
    if sides[0] + sides[1] <= sides[2]:
        print("Invalid")
    elif sides[0] == sides[1] == sides[2]:
        print("Equilateral")
    elif (sides[0] == sides[1]) | (sides[0] == sides[2]) | (sides[1] == sides[2]):
        print("Isosceles")
    elif (sides[0] != sides[1]) | (sides[0] != sides[2]) | (sides[1] != sides[2]):
        print("Scalene")
    