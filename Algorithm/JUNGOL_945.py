anime = {'Pokemon':'Pikachu', 'Digimon':'Agumon', 'Yugioh':'Black Magician'}

name = input()

#print(anime[name] if name in anime else "I don't know")
print(anime.get(name, "I don't know"))