t = int(input())

for i in range(t):
    math_input = input().replace('@', '* 3').replace('%', '+ 5').replace('#', '- 7')
    print(float(eval(math_input)))