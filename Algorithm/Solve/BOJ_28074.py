word = set(input())
mobis = set("MOBIS")

if mobis - word == set():
    print("YES")
else:
    print("NO")