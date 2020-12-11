from copy import deepcopy

my_data = [   # create a nested list object and assign 'my_data' to it
    ['a', 'b', 'c'],
    [1, 2, 3],
    ['wombat', 'honey badger', 'platypus'],
]

print(type(my_data), type(my_data[0]), type(my_data[0][0]), '\n')

for thing in my_data:
    print(thing)
print()

a = my_data  #  assign 'a' to same object as 'my_data'
print(a[2][1], '\n')

print(id(my_data), id(a))

my_data.append(['red', 'blue', 'green'])
print(a, '\n')

print(type(a))

b = list(my_data)  # shallow copy
print(id(my_data), id(a), id(b))

my_data.append(["Montreal", "Houston", "Allentown"])
print(my_data)
print(a)
print(b)

my_data[2].append("pine marten")

print(my_data)
print(a)
print(b)

c = deepcopy(my_data)
print(id(my_data), id(a), id(b), id(c), '\n')
my_data[2].append("cane toad")
print(my_data)
print(a)
print(b)
print(c)



airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

a2 = airports
a2['ELM'] = 'Elmyra'
print(airports)

a3 = dict(airports)
a3['PHX'] = 'Phoenix Sky Harbor'

print(airports)
print(a3)




