a = int(input())
t = int(input())
w = input()

default = "0101"
person = 0
time = 1

while t > 0:
    words = default + ("0" * (time + 1)) + ("1" * (time + 1))
    time += 1

    for word in words:
        person += 1

        if person == a:
            person = 0

        if word == w:
            t -= 1
        
        if t == 0:
            break

if person == 0:
    person = a - 1
else:
    person -= 1

print(person)
    