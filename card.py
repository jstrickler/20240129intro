class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit

    # called when this object passed to str()
    def __str__(self):  # human-friendly
        return f"{self.rank}-{self.suit}"

    def __repr__(self):  # code-friendly
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":  # if executed as a script
    c1 = Card("5", "Diamonds")
    c2 = Card("8", 'Spades')

    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    print(c1, c2)
    print(repr(c1))
    print(f"{c1 = }")
    

    