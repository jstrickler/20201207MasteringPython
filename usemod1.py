import sys
# from pkg.pkg import module
from myproject.db import john
from myproject.wombat.snuffle import snuffling

snuffling()


def spam():
    print("Not so awkward")

# module.function()
# module.class
# module.variable
john.spam()
john.ham()
spam()

print(john.ANIMALS)
print(john.ANIMALS[0])

for path in sys.path:
    print(path)
