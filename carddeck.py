import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamond Hearts Spades'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return tuple(self._cards)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()
    
    def __len__(self):  # used with len(x)
        return len(self._cards)

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}:{len(self)}"

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"

if __name__ == "__main__":
    d1 = CardDeck()
    print(d1)
    d1.shuffle()
    print(d1.cards)

    for _ in range(5):
        c = d1.draw()
        print(c.rank, c.suit)

    print(d1)
    print(f"{len(d1) = }")
    print(f"{d1 = }")
    