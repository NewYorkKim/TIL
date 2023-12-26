import sys
input = sys.stdin.readline

def back(idx, vowel, consonant):
    if len(ans) == n:
        if vowel >= 1 and consonant >= 2:
            print("".join(ans))
        return 

    for i in range(idx, m):
        if words[i] not in ans:
            ans.append(words[i])
            if words[i] in vowels:
                back(i, vowel+1, consonant)
            else:
                back(i, vowel, consonant+1)
            ans.pop()

n, m = map(int, input().split())
words = sorted(input().split())
vowels = ["a", "e", "i", "o", "u"]
ans = []

back(0, 0, 0)