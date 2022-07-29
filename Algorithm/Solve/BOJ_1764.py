n, m = map(int, input().split())

none_heard = set()
for i in range(n):
    none_heard.add(input())

none_seen = set()
for i in range(m):
    none_seen.add(input())

none_seen_heard = sorted(none_heard & none_seen)

print(len(none_seen_heard), *none_seen_heard, sep='\n')



