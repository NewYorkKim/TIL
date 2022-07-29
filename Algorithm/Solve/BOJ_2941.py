# c_words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# get_words = input()
# total = len(get_words)

# for word in c_words:
#     total -= get_words.count(word)

# print(total)

words = input()
result = len(words) - sum(map(words.count, ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='])) 
print(result)  