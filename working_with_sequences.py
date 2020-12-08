


cities = ['Montreal', 'Houston', 'Jersey City', 'Des Moines']


print(len(cities), min(cities), max(cities), sorted(cities))


nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

s = sum(nums)
print("s:", s, '\n')

for city in reversed(cities):
    print(city)
print()

s_or_p = ['Quebec', 'Texas', 'New Jersey', 'Iowa']

for s, p in zip(cities, s_or_p):
    print(s, p)

print(list(zip(cities, s_or_p)))

places = list(zip(cities, s_or_p))

print(places)

x = list('abc')
print(x)

z1 = zip(cities, s_or_p)
print(z1)

r1 = reversed(cities)
print(r1)
print()

#  GENERATOR!!!

print("round 1")
for city in r1:
    print(city)
print()

print("round 2")
for city in r1:
    print(city)
print()











