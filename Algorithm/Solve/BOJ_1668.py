n = int(input())
places = [int(input()) for _ in range(n)]
left, right = 1, 1
previous_left, previous_right = places[0], places[-1]

for i in range(n):
    if places[i] > previous_left:
        left += 1
        previous_left = places[i]
    if places[-1-(i)] > previous_right:
        right += 1
        previous_right = places[-1-(i)]

print(left)
print(right)