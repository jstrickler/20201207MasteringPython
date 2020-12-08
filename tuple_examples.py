
person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

print(type(person), person[0], person[:2])

first_name, last_name, product, dob = person

cs = "Des Moines,IA"

city, state = cs.split(',')
print(f"{city} is in {state}\n")

x = ['a', 'b']

j, k = x  # unpacking iterable x into list of variables
print(f"j is {j} k is {k}\n")

word = 'spam'

w1, w2, w3, w4 = word

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z, '\n')

x, *y, z = values
print(x, y, z, '\n')

*x, y, z = values
print(x, y, z, '\n')

x, y, z = values[0], values[2], values[-1]


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]

for person in people:
    # first_name, last_name, product, dob = person
    print(person)
print('-' * 60)

for first_name, last_name, *product, dob in people:  # unpacking!!
    # first_name, last_name, product, dob = <next element of people>
    print(first_name, last_name, product)
print('-' * 60)





