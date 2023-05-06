cocktails = list(map(int, input().split()))
ans = 1
odd = False

for cocktail in cocktails:
    if cocktail % 2 != 0:
        odd = True
        ans *= cocktail

if odd == True:
    print(ans)
else:
    ans = cocktails[0] * cocktails[1] * cocktails[2]
    print(ans)