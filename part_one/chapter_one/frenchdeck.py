from collections import namedtuple
from random import choice


Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit)
            for rank in self.ranks
            for suit in self.suits
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, idx):
        return self._cards[idx]


if __name__ == "__main__":
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(f"{len(deck) = }")
    print(f"{choice(deck) = }")
    print(f"{deck[-1] = }")

    i = 0
    for card in deck:   # works due to __getitem__
        print(card)
        i += 1
        if i == 4:
            break

    # works not because of __contains__ but because it is iterable
    print(f"{Card('Q', 'spades') in deck = }")
