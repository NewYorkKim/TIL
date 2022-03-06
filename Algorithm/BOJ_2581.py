m = int(input())
n = int(input())
result = [number for number in range(m, n + 1) if number != 1 and all(number % i for i in range(2, number))]

# if len(result) > 0:
#     print(sum(result))
#     print(min(result))
# else:
#     print(-1)

print(f"{sum(result)}\n{min(result)}" if len(result) > 0 else -1)