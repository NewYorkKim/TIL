from itertools import combinations

heights = [int(input()) for _ in range(9)]

# for i in range(9):
#     for j in range(i + 1, 9):
#         if sum(heights) - (heights[i] + heights[j]) == 100:
#             temp1 = heights[i]
#             temp2 = heights[j]
#             break

# heights.remove(temp1)
# heights.remove(temp2)

# print(*sorted(heights), sep='\n')

print(*[sorted(dwarf) for dwarf in combinations(heights, 7) if sum(dwarf) == 100][0])
