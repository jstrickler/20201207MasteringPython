fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

# non-Pythonic
f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

#  [EXPR for VAR in ITERABLE if CONDITION]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam', 'toast',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]

nonspam = [f for f in food if f != 'spam']
print("nonspam: {}\n".format(nonspam))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [float(n) * 10 for n in nums if n > 300]
print("n1: {}\n".format(n1))

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

last_names = [p[1] for p in people]
print("last_names: {}\n".format(last_names))

last_names = [p[1] for p in people if p[0].startswith('L')]
print("last_names: {}\n".format(last_names))

# RESULT_LIST = [EXPR_FOR_THE_CURRENT_VARIABLE for VAR in SOME_ITERABLE if SOME_CONDITION]

last_names = []
for p in people:
    if p[0].startswith('L'):
        last_names.append(p[1])
print("last_names: {}\n".format(last_names))

ln_gen = (p[1] for p in people)  # generator expression
print(ln_gen)

for last_name in ln_gen:
    print(last_name)
print()

print("2nd time")
for last_name in ln_gen:
    print(last_name)
print()

