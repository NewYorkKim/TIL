v = int(input())
voting = input()

a = voting.count('A')
b = voting.count('B')

if a > b:
    print('A')
elif a == b:
    print('Tie')
else:
    print('B')