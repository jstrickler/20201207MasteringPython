from carddeck import CardDeck

class LeisureItem():
    def play(self):
        print("playing....")

class JokerDeck(CardDeck, LeisureItem):  # JokerDeck inherits from CardDeck

    def _make_deck(self):
        super()._make_deck()
        joker1 = ('1', 'JOKER')
        joker2 = ('2', 'JOKER')
        self._cards.append(joker1)
        self._cards.append(joker2)
