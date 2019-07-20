from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return f'FrenchDeck {id(self)}'

    def __str__(self):
       return f'FrenchDeck has {len(self)} cards.'


if __name__ == '__main__':
    deck = FrenchDeck()
    print(deck)
    #print(len(deck))
    #print(str(deck))

