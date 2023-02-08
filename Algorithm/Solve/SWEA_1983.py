t = int(input())
marks = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for i in range(1, t+1):
    n, k = map(int, input().split())
    grades = dict()
    for j in range(1, n+1):
        m, f, a = map(int, input().split())
        grades[j] = m*0.35 + f*0.45 + a*0.2
    grades = list(sorted(grades, key = lambda x: grades[x], reverse=True))
    idx = int(grades.index(k) / (len(grades) // 10)) 
    print(f'#{i}', marks[idx])

