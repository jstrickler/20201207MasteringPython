
def get_message():
    message = "Hello, world"
    return message

m = get_message()  # call (evaluate) function -- get return value

print(get_message() + "XXXXX")

x = get_message  # just a copy of the actual function

print(x)

def print_message():
    msg = get_message()
    print(msg)

print_message()
print()


def greet(whom="world"):
    print("Hello,", whom)

greet("world")
greet("Python")
greet("Dolly")

greetee = "Bob"

greet(greetee)

# greet("Fred", "Ethel")

greet()

def find_words(filename, *words):
    print("words:", words)
    for word in words:
        print("looking for {} in {}".format(word, filename))

find_words('foo.txt', 'wombat')
find_words('foo.txt', 'wombat', 'tapir')
find_words('foo.txt')

foo = ['a', 'b', 'c']

def add_something(alist):
    alist.append('wombat')


add_something(foo)

print(foo)









