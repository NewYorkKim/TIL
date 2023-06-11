import sys
input = sys.stdin.readline

n = int(input())
people = set()

for _ in range(n):
    name, status = input().split()

    if status == "enter":
        people.add(name)
    else:
        if name in people:
            people.remove(name)

people = sorted(people, reverse=True)

for person in people:
    print(person)