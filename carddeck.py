import random

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._make_deck()


    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)


    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):  # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")


    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

