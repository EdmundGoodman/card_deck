#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Provides Card, Pile, and Deck classes for modelling cards, with Suits and
Faces enums as backend data structures

Suits and Faces are enums containing the names and values of their respective
items. Card models a single card, Pile models an ordered list of cards of
arbitrary length, and Deck models a Pile of cards containing every permutation
of suit and face, initially ordered by the enum values.
"""

from functools import total_ordering
from enum import Enum, unique
import random

__author__ = "Edmund Goodman"
__copyright__ = "Copyright 2020, Edmund Goodman"
__credits__ = ["Edmund Goodman"]
__license__ = "MIT"
__maintainer__ = "Edmund Goodman"
__email__ = "egoodman3141@gmail.com"


@unique
class Suits(Enum):
    """An Enum class for the suits in of a card"""
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4


@unique
class Faces(Enum):
    """An Enum class for the faces of a card"""
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class CardError(Exception):
    """A custom exception to indicate an error occuring in the Card class"""


class PileError(Exception):
    """A custom exception to indicate an error occuring in the Pile class"""


@total_ordering
class Card:
    """A model of a card as having a Face and a Suit, a printeable and a
    typeable name, and value with respect other cards"""

    LOOKUP_FACE_CHAR = {f: "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")[i]
                        for i, f in enumerate(Faces)}
    LOOKUP_SUIT_CHAR = {s: '♦,♣,♥,♠'.split(",")[i]
                        for i, s in enumerate(Suits)}
    LOOKUP_SUIT_LETTER = {s: s.name[0] for s in Suits}

    LOOKUP_FACE_TYPEABLE = {v: k for k, v in LOOKUP_FACE_CHAR.items()}
    LOOKUP_SUIT_TYPEABLE = {v: k for k, v in LOOKUP_SUIT_LETTER.items()}

    def __init__(self, face, suit):
        """Initialise the card as having a Face and a Suit"""
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Get the Face of the card"""
        return self._face

    @face.setter
    def face(self, value):
        """Raise an error on trying to change the Face of a card"""
        raise CardError("'Card.face' property does not support assignment")

    @property
    def suit(self):
        """Get the Suit of the card"""
        return self._suit

    @suit.setter
    def suit(self, value):
        """Raise an error on trying to change the Face of a card"""
        raise CardError("'Card.suit' property does not support assignment")

    @staticmethod
    def get_from_typeable_name(typeable_name):
        """Return the Card object specified by the typeable name. If the name
        does not reference a valid card, return None

        The first character of this string represents the face, as either the
        first letter of the face name if it is a picture card, or the number
        of the face if it is not. The second character of this string reprsents
        the suit, as the first letter of the suit name.
        For example, the ace of hearts would be 'AH', whereas the five of clubs
        would be '5C'"""
        if len(typeable_name) == 2:
            face_char, suit_char = typeable_name[0], typeable_name[1].upper()
            face, suit = None, None
        else:
            return None

        if face_char in Card.LOOKUP_FACE_TYPEABLE:
            face = Card.LOOKUP_FACE_TYPEABLE[face_char]
        else:
            raise CardError("Cannot build card with invalid face: '{}'".format(
                            face_char))
        if suit_char in Card.LOOKUP_SUIT_TYPEABLE:
            suit = Card.LOOKUP_SUIT_TYPEABLE[suit_char]
        else:
            raise CardError("Cannot build card with invalid suit: '{}'".format(
                            face_char))

        return Card(face, suit)

    def get_typeable_name(self):
        """Get the typeable name of the card, i.e. a unique string to describe
        a card's value"""
        return (Card.LOOKUP_FACE_CHAR[self._face]
                + Card.LOOKUP_SUIT_LETTER[self._suit])

    def __eq__(self, other):
        """Return the equality between two cards"""
        return self._face == other.face and self._suit == other.suit

    def __lt__(self, other):
        """Return whether the card has a lower value than another card, first
        by comparing faces, then if they are equal by comparing suits"""
        if self._face < other.face:
            return True

        return self._suit < other.suit

    def __hash__(self):
        """Generate a unique integer representation of the card"""
        return hash(str(self._face.value)+str(self._suit.value))

    def __str__(self):
        """Use the string representation of the card as the informal
        representation of the card"""
        return (Card.LOOKUP_FACE_CHAR[self._face]
                + Card.LOOKUP_SUIT_CHAR[self._suit])

    def __repr__(self):
        """Get a string representing the card, using UTF-8 characters to
        prettily denote the suit"""
        return str(self)


@total_ordering
class Pile:
    """A Pile object, which represents an ordered list of cards of arbitrary
    length"""

    def __init__(self, cards=None):
        """Initialise the pile by default as empty, or with a specified list
        of initial cards"""
        if cards is None:
            self._cards = []
        else:
            self._cards = cards

    @property
    def cards(self):
        """Get the list of cards in the pile"""
        return self._cards

    @cards.setter
    def cards(self, cards):
        """Set the list of cards in the pile"""
        self._cards = cards

    def pop(self):
        """Pop a card off the top of the pile"""
        if self.empty():
            raise PileError("Cannot pop card from empty pile")
        return self._cards.pop()

    def remove(self, card):
        """Remove a card from the Pile"""
        if card not in self._cards:
            raise PileError(
                    "Cannot remove '{}' as it is not in the pile".format(card))
        self._cards.remove(card)

    def peek(self, position=-1):
        """Peek at the value of a card in the pile, by default the top card, or
        at a specified position in the pile"""
        return self._cards[position]

    def insert(self, card, position=None):
        """Place a card into the pile, by default to the top, or at a specified
        position in the pile"""
        if position is None:
            position = len(self._cards)
        self._cards.insert(position, card)

    def append(self, card):
        """Append the card to the Pile"""
        self._cards.append(card)

    def shuffle(self):
        """Randomly shuffle the order of the cards in the pile"""
        random.shuffle(self._cards)

    def sort(self):
        """Sort the pile of cards in the total ordering of the cards"""
        self._cards.sort()

    def deal(self, num_sets, num_cards):
        """Deal cards from the pile into a specified number of new piles,
        each containing a specified number of cards. If there are more cards
        required to fill the piles than there are in the current pile, stop
        when the current pile is empty, and return the piles, irrespective
        of the fact they are not totally filled"""
        sets = [Pile() for _ in range(num_sets)]
        for _ in range(num_cards):
            for j in range(num_sets):
                try:
                    sets[j].insert(self.pop())
                except IndexError:
                    return sets
        return sets

    def clear(self):
        """Empty the contents of the Pile"""
        self._cards = []

    def count(self, card):
        """Count the number of instances of a card in the Pile"""
        return self._cards.count(card)

    def size(self):
        """Return the number of cards in the pile"""
        return len(self._cards)

    def empty(self):
        """Return whether the pile is empty"""
        return self.size() == 0

    def copy(self):
        """Return a copy of the Pile"""
        return Pile(self._cards)

    def extend(self, other):
        """Extend the pile contents by another pile"""
        self._cards = self.cards + other.cards

    def reverse(self):
        """Reverse the order of the Pile"""
        self._cards.reverse()

    def __add__(self, other):
        """Concatenate a pile to the end of the current pile"""
        return Pile(self._cards.extend(other.cards))

    def __sub__(self, other):
        """Remove all cards from the current pile that are in the other pile
        (take the relative complement of the current and other piles)"""
        return Pile([item for item in self if item not in other])

    def __iter__(self):
        """Create an iterator for the pile of cards"""
        for card in self._cards:
            yield card

    def __contains__(self, item):
        """Return whether the pile contains a specified card"""
        return item in self._cards

    def __len__(self):
        """Get the size of the pile"""
        return len(self._cards)

    def __getitem__(self, position):
        """Get the item at an index in the Pile"""
        return self._cards[position]

    def __reversed__(self):
        """Return a new Pile of the current cards, but in reverse order"""
        return Pile(self._cards[::-1])

    def __and__(self, other):
        """Return the intersection of the current and another pile of cards"""
        return Pile([item for item in self._cards if item in other.cards])

    def __or__(self, other):
        """Return the union of the current and another pile of cards"""
        return Pile(list(set(self._cards).union(set(other.cards))))

    def __xor__(self, other):
        return (self or other) - (self and other)

    def __eq__(self, other):
        """Return whether two piles are equal (i.e. contain the same cards
        in the same order)"""
        return self._cards == other.cards

    def __lt__(self, other):
        """Return whether this pile is smaller than the other pile"""
        return len(self) < len(other)

    def __hash__(self):
        """Generate a unique integer representation of the pile"""
        return hash("".join([str(hash(x)) for x in self._cards]))

    def __str__(self):
        """Use the string representation of the pile as the informal
        representation of the pile"""
        return ", ".join([str(x) for x in self._cards])

    def __repr__(self):
        """Return a string representation of the pile, formatted as a list
        of the string representations of the cards it holds"""
        return str(self)


class Deck(Pile):
    """A Deck object, which is a Pile object that is initialised with
    every permutation of suit and face, initially ordered by the enum values"""
    def __init__(self):
        Pile.__init__(self)
        for suit in Suits:
            for face in Faces:
                self._cards.append(Card(face, suit))


if __name__ == "__main__":
    import copy

    # Test getting the typeable name of a card
    print(Card(Faces.SIX, Suits.SPADES).get_typeable_name())

    # Test gettting a card form its typeable name
    while True:
        inp = str(input("Enter the typeable name of a card: "))
        card = Card.get_from_typeable_name(inp)
        if card is not None:
            break
    print(card)

    # Test making Decks and Pile
    d1 = Deck()
    d2 = Pile([Card(Faces.ACE, Suits.DIAMONDS)])
    d3 = Pile([
        Card(Faces.ACE, Suits.HEARTS),
        Card(Faces.FIVE, Suits.CLUBS),
    ])

    # Test operations on Decks and Piles
    print(dir(d1))
    print(d1)
    print(d2)
    print(d1 - d2)
    print(d1 ^ d2)
    print(d1 and d3)
    print(d1 is copy.deepcopy(d1))

    # Test the hash functions of Pile objects
    print(hash(d1))
    print(hash(d2))
