from itertools import chain

list1 = list()   # empty list
list2 = ['a', 'b', 'c']   # initialized from items
list3 = []   # empty list
list4 = "spam ham eggs toast".split()

print(list1, list2, list3, list4, '\n')


cities = ['Montreal', 'Houston', 'Jersey City', 'Des Moines']

print(cities)
print(cities[0], cities[2], cities[-1], cities[len(cities) - 1], sep=', ')

cities.append('Frederick')
print(cities, '\n')

spam = [1, 2, 3]

cities.append(spam)

print(cities, '\n')

cities.insert(0, 'Montreal')
cities.insert(4, 'Allentown')

print(cities, '\n')

more_cities = ['Durham', 'Toronto', 'Vancouver']
other_cities = ['Dallas', 'Kitchener', 'New Orleans']

cities.extend(chain(more_cities, other_cities))  # add individually

print(cities, '\n')

print(len(cities), '\n')

del cities[7]

print(cities, '\n')

x = 5
del x  # x goes away

c = cities.pop(3)
print(c)

print(cities, '\n')

c = cities.pop()  # pop the LAST item

print(c)
print(cities, '\n')

cities.remove('Vancouver')

city = 'Topeka'
if city in cities:
    cities.remove(city)

print(cities, '\n')

cities.remove('Montreal')
print(cities, '\n')


print(cities[0], cities[5], cities[-1], cities[-4], '\n')

print(cities[0:4])   # slice[start:end]

#  [start:stop]  [:stop]  [start:]  [start:stop:step]

# start is INclusive
# stop is EXclusive

print(cities[3:6], '\n')

print(cities[:4])
print(cities[6:])

print(cities[-3:])  # last 3

start = 2
stop = 7

print(cities[start:stop], '\n')

#  for VAR in ITERABLE:
for city in cities:
    print(city)
print('=' * 50)

# NOT pythonic!
#  this is the C/C++/Java/Kotlin/etc way
# i = 0
# while i < len(cities):
#     print(cities[i])
#     i += 1

s = "abc"

for char in s:
    print(char)
print()

b = b'\01\02\03'

for byte in b:
    print(byte)
print()

# str bytes list tuple set dict *generator*










