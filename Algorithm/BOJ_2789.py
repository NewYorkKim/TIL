word = input()

print(''.join(w for w in word if w not in 'CAMBRIDGE'))

# word = input()

# for w in 'CAMBRIDGE':
#     word = word.replace(w, '')

# print(word)