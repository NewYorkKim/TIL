n = int(input())
words = [input() for _ in range(n)]
words = sorted(set(words), key=lambda x: (len(x), x))

print(*words, sep='\n')