# n, m = map(int, input().split())
# passwords = dict()

# for _ in range(n):
#     url, password = input().split()
#     passwords[url] = password

# for _ in range(m):
#     where = input()
#     print(passwords[where])

n, m = map(int, input().split())
passwords = dict()

for _ in range(n):
    url, password = input().split()
    passwords[hash(url)] = password

for _ in range(m):
    url = input()
    print(passwords[hash(url)])