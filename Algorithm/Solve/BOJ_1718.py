plain = input()
key = input() * len(plain)
encrypted = ""

for i in range(len(plain)):
    if plain[i] == " ":
        encrypted += " "
        continue
    diff = ord(key[i]) - 96
    if ord(plain[i]) - diff < 97:
        encrypted += chr(122 + ((ord(plain[i]) - diff) - 96))
    else:
        encrypted += chr(ord(plain[i]) - diff)

print(encrypted)