h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

if s2 >= s1:
    s = s2 - s1
else: 
    s = (s2 + 60) - s1
    m2 -= 1

if m2 >= m1:
    m = m2 - m1
else:
    m = (m2 + 60) - m1
    h2 -= 1

if h2 >= h1:
    h = h2 - h1
else:
    h = (24 - h1) + h2

if (s == 0) & (m == 0) & (h == 0):
    h = 24

print(f"{str(h):0>2}:{str(m):0>2}:{str(s):0>2}")