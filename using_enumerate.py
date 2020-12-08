

cities = ['Montreal', 'Houston', 'Jersey City', 'Des Moines']

for city in cities:
    print(city)
print()

# i = 0
# while i < len(cities):
#     print(cities[i])
#     i += 1

for i, city in enumerate(cities):
    print(i, city)
print()

print(list(enumerate(cities)), '\n')


