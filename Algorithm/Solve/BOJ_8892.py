t = int(input())

for i in range(t):
    k = int(input())
    words = []
    cnt = 0

    for j in range(k):
        words.append(input())

    for l in range(k):
        for m in range(k):
            if l != m:
                new = words[l] + words[m]
                if new == new[::-1]:
                    print(new)
                    cnt += 1
                    break
    if cnt == 0:
        print(0)

# from itertools import permutations

# t = int(input())

# for i in range(t):
#     k = int(input())
#     words = []

#     for j in range(k):
#         words.append(input())

#     for word1, word2 in permutations(words, 2):
#         new = word1 + word2
#         if new == new[::-1]:
#             print(new)
#             break
#     else:
#         print(0)