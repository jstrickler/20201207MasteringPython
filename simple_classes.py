
class Dog:  # inherits from object

    def __init__(self, name, breed):
        self._name = name  # store name for later use
        self._breed = breed

    @property
    def name(self):
        return self._name

    @property
    def breed(self):
        return self._breed

    def bark(self):
        print("Woof! Woof!")

d1 = Dog('Andy', 'Mutt')  #  Dog d1 = new Dog('Andy', 'Mutt');
d2 = Dog('Nellie', 'English Shepherd')
d3 = Dog('Frodo', 'German Shepherd')

print(type(d1))

d1.bark()   # same as Dog.bark(d1)
d2.bark()

print(d1.name, d1.breed)
print(d2.name)
print(d3.breed)

