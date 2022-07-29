# dice = list(map(int, input().split()))
# result = [dice.count(i) for i in dice]
# most = max(result)

# if most == 3:
#     print(10000 + dice[0] * 1000)
# elif most == 2:
#     print(1000 + dice[result.index(most)] * 100)
# else:
#     print(max(dice) * 100)

first, second, third = sorted(map(int, input().split()))
print([third, second + 10, second * 10 + 100][[first, second, third].count(second) - 1] * 100)