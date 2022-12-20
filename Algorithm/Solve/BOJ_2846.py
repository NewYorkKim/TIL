# a, b = input().split()

# a1, b1 = int(a.replace('6', '5')), int(b.replace('6', '5'))
# a2, b2 = int(a.replace('5', '6')), int(b.replace('5', '6'))

# print(a1+b1, a2+b2)

s = input().replace(' ', '+')
print(eval(s.replace('6', '5')), eval(s.replace('5', '6')))