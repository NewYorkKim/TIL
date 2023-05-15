students = [i+1 for i in range(30)]

for j in range(28):
    n = int(input())
    studnets = students.remove(n)

for student in students:
    print(student)