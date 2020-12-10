from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Alfred")
d2 = CardDeck("Marina")
j1 = JokerDeck('Bob')

print(j1.dealer)
j1.shuffle()
print(j1.draw())


print(d1.dealer)

d1.dealer = "Benito"

d1.shuffle()   #  CardDeck.shuffle(d1)
print(d1.cards, '\n')

for i in range(5):
    print(d1.draw())
print()


try:
    d1.dealer = 42.9
except TypeError as err:
    print(err)

try:
    d3 = CardDeck(55)
except TypeError as err:
    print(err)

print(d1.get_ranks())

print(CardDeck.get_ranks())

print(j1.cards, '\n')
j1.play()

print(JokerDeck.mro())
