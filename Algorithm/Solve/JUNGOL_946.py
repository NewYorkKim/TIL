capital = dict()
n = int(input())

for i in range(n):
    country, city = input().split()
    capital[country] = city

where = input()
print(capital[where] if where in capital else 'Unkown Country')