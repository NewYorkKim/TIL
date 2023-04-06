import math

n = int(input())
nums = list(map(int, input().split()))
result = []

g = math.gcd(nums[0], math.gcd(nums[1], nums[-1]))

for i in range(1, g//2 + 1):
    if g % i == 0:
        result.append(i)
        
result.append(g)

for j in result:
    print(j)