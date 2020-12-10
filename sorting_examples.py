fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0: {}\n".format(f0))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
n0 = sorted(nums)
print("n0: {}\n".format(n0))

data = [('m', 5), ('d', 18), ('m', 3), ('f', 12), ('a', 99)]
d0 = sorted(data)
print("d0: {}\n".format(d0))

#  s = str.lower(x)

print(str.lower("WHOOPEEE"), '\n')

f1 = sorted(fruits, key=str.lower)
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=len)  # apply len() to each element of fruits
print("f2: {}\n".format(f2))

def by_value(element):
    return element[0]

d1 = sorted(data, key=by_value)  # sorted() will call by_value() on each individual element
print("d1: {}\n".format(d1))

def custom_sort(e):
    return len(e), e.lower()

f3 = sorted(fruits, key=custom_sort)    #  'custom_sort' is a CALLBACK
print("f3: {}\n".format(f3))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(person):
    year, month, day = person[3].split('-')
    return month, year

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

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

for code, name in sorted(airports.items()):
    print(code, name)
print('-' * 60)

def by_value(dict_element):
    key, value = dict_element
    return value

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print('-' * 60)



print(list(airports.items()))


f4 = sorted(fruits, reverse=True)
print("f4: {}\n".format(f4))

n1 = sorted(nums, reverse=True)
print("n1: {}\n".format(n1))

for code, name in sorted(airports.items(), key=lambda e: e[1]):
    print(code, name)
print('-' * 60)

#  lambda param: <return value>

def foo(e):
    return e[1]
