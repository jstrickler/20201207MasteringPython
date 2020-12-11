from collections import namedtuple
from pprint import pprint

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(person[0], person[1])

person = {
    'firstname': 'Bill',
    'lastname': 'Gates',
    'product': 'Microsoft',
    'dob': '1955-10-28',
}

print(person['firstname'], person['lastname'])


Person = namedtuple('Person', 'first_name last_name product dob')

person = Person('Bill', 'Gates', 'Microsoft', '1955-10-28')
print(person[0], person[1])
print(person.first_name, person.last_name)

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


person_list = [Person(*p) for p in people]

# print(person_list)

for person in person_list:
    print(person.first_name, person.last_name)



def doit(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)

doit(1, 2, 3)

args = [5, 10, 20]

doit(args[0], args[1], args[2])
doit(*args)

print()

pprint(person_list)






