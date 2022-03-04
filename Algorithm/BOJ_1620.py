n, m = map(int, input().split())

pokemon = dict()

for i in range(n):
    pokemon[str(i + 1)] = input()

reversed_pokemon = {name:number for number, name in pokemon.items()}

for j in range(m):
    problem = input()
    if problem in pokemon.keys():
        print(pokemon[problem])
    else:
        print(reversed_pokemon[problem])
