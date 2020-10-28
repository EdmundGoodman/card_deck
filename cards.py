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

    def __doc__(self):
        """Return a string summary of the class"""
        return "An Enum object for the Suits of a card"


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

    def __doc__(self):
        """Return a string summary of the class"""
        return "An Enum object for the Faces of a card"



class CardLookupData:
    """Utility class storing data to lookup how to print cards, and
    accept them as typeable characters"""
    FACE_LOOKUP_TYPEABLE = {str(f.value):f for f in Faces
                            if f.value not in [1,11,12,13]}
    FACE_LOOKUP_TYPEABLE.update({str(f.name)[0]:f for f in Faces
                                if f.value in [1,11,12,13]})
    SUIT_LOOKUP_TYPEABLE = {s.name[0]:s for s in Suits}

    FACE_LOOKUP_CHAR = {f:"A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")[i]
                        for i,f in enumerate(Faces)}
    SUIT_LOOKUP_CHAR = {f:'♦,♣,♥,♠'.split(",")[i]
                        for i,f in enumerate(Suits)}

    def __doc__(self):
        """Return a string summary of the class"""
        return """A utility class storing lookup data about cards"""


@total_ordering #Only need to define __eq__ and __lt__ for all comparisons
class Card:
    """A model of a card as having a Face and a Suit, a printeable and a
    typeable name, and value with respect other cards"""

    def __init__(self, face, suit):
        """Initialise the card as having a Face and a Suit"""
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Get the Face of the card"""
        return self._face

    @face.setter
    def face(self):
        """Raise an error on trying to change the Face of a card"""
        raise ValueError("'Card.face' property does not support assignment")

    @property
    def suit(self):
        """Get the Suit of the card"""
        return self._suit

    @suit.setter
    def suit(self):
        """Raise an error on trying to change the Face of a card"""
        raise ValueError("'Card.suit' property does not support assignment")

    def getTypeableName(self):
        """Get the typeable name of the card, i.e. a unique string to describe
        a card's value.
        The first character of this string represents the face, as either the
        first letter of the face name if it is a picture card, or the number
        of the face if it is not. The second character of this string reprsents
        the suit, as the first letter of the suit name.
        For example, the ace of hearts would be 'AH', whereas the five of clubs
        would be '5C'"""
        faceNum = self._face.value
        suitChar = self._suit.name[0]
        if faceNum in [1,11,12,13]:
            faceChar = self._face.name[0]
        else:
            faceChar = str(faceNum)
        return faceChar + suitChar

    def __eq__(self, other):
        """Return the equality between two cards"""
        return self._face == other.face and self._suit == other.suit

    def __lt__(self, other):
        """Return whether the card has a lower value than another card, first
        by comparing faces, then if they are equal by comparing suits"""
        if self._face < other.face:
            return True
        else:
            return self._suit < other.suit

    def __hash__(self):
        """Generate a unique integer representation of the card"""
        return hash(str(self._face.value)+str(self._suit.value))

    def __str__(self):
        """Use the string representation of the card as the informal
        representation of the card"""
        faceStr = CardLookupData.FACE_LOOKUP_CHAR[self._face]
        suitStr = CardLookupData.SUIT_LOOKUP_CHAR[self._suit]
        return faceStr + suitStr

    def __repr__(self):
        """Get a string representing the card, using UTF-8 characters to
        prettily denote the suit"""
        return str(self)

    def __doc__(self):
        """Return a string summary of the class"""
        return """An immutable object representing a card, requires arguments
which are instances of the Face and Suit enums"""


class CardFromTypeableName:
    """A utility class to generate a Card object from its typeable name,
    to streamline data entry of cards via a text format"""

    def getCard(self, typeableName):
        """Return the Card object specified by the typeable name. If the name
        does not reference a valid card, return None"""
        faceChar, suitChar = typeableName[0], typeableName[1]
        face, suit = None, None

        if faceChar in CardLookupData.FACE_LOOKUP_TYPEABLE:
            face = CardLookupData.FACE_LOOKUP_TYPEABLE[faceChar]
        if suitChar in CardLookupData.SUIT_LOOKUP_TYPEABLE:
            suit = CardLookupData.SUIT_LOOKUP_TYPEABLE[suitChar]

        if len(typeableName) == 2 and face is not None and suit is not None:
            return Card(face, suit)
        else:
            return None

    def __doc__(self):
        """Return a string summary of the class"""
        return "A utility class to generate a Card from its typeable name"


@total_ordering #Only need to define __eq__ and __lt__ for all comparisons
class Pile:
    """A Pile object, which represents an ordered list of cards of arbitrary
    length"""

    def __init__(self, cards=[]):
        """Initialise the pile by default as empty, or with a specified list
        of initial cards"""
        self._cards = cards

    @property
    def cards(self):
        """Get the list of cards in the pile"""
        return self._cards

    @cards.setter
    def cards(self, cards):
        """Set the list of cards in the pile"""
        self._cards = cards

    def pop(self, position=None):
        """Pop a card off the pile, by default from the top, or at a specified
        position in the pile"""
        if position is None:
            position = len(self._cards) - 1
        return self._cards.pop()

    def remove(self, card):
        """Remove a card from the Pile"""
        self._card.remove(card)

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

    def deal(self, numSets, numCards):
        """Deal cards from the pile into a specified number of new piles,
        each containing a specified number of cards. If there are more cards
        required to fill the piles than there are in the current pile, stop
        when the current pile is empty, and return the piles, irrespective
        of the fact they are not totally filled"""
        sets = [Pile() for n in range(numSets)]
        for i in range(numCards):
            for j in range(numSets):
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

    def copy(self):
        """Return a copy of the Pile"""
        return Pile(self._cards)

    def extend(self, other):
        """Extend the pile contents by another pile"""
        self._cards = self.cards + other.cards

    def reverse(self):
        """Reverse the order of the Pile"""
        self._cards.reverse()

    def sort(self):
        """Sort the Pile into ascending order"""
        self._cards.sort()

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

    def __doc__(self):
        """Return a string summary of the class"""
        return """A mutable sequence of cards. If no argument is given the
constructor creates an empty pile. The argument must be iterable if specified"""



class Deck(Pile):
    """A Deck object, which is a Pile object that is initialised with
    every permutation of suit and face, initially ordered by the enum values"""
    def __init__(self):
        Pile.__init__(self)
        for suit in Suits:
            for face in Faces:
                self._cards.append(Card(face, suit))

    def __doc__(self):
        """Return a string summary of the class"""
        return """A child of the Pile class, which is constructed containing
all the cards in a single deck in order"""



if __name__=="__main__":
    """Test the interfaces of the objects"""
    import copy

    #Test getting the typeable name of a card
    print(Card(Faces.SIX, Suits.SPADES).getTypeableName())

    #Test gettting a card form its typeable name
    while True:
        inp = str(input("Enter the typeable name of a card: "))
        card = CardFromTypeableName().getCard(inp)
        if card is not None:
            break
    print(card)



    #Test making Decks and Pile
    d1 = Deck()
    d2 = Pile([Card(Faces.ACE, Suits.DIAMONDS)])
    d3 = Pile([
        Card(Faces.ACE, Suits.HEARTS),
        Card(Faces.FIVE, Suits.CLUBS),
    ])

    #Test operations on Decks and Piles
    print(dir(d1))
    print(Card.__doc__(Card))
    print(d1)
    print(d2)
    print(d1 - d2)
    print(d1 ^ d2)
    print(d1 and d3)
    print(d1 is copy.deepcopy(d1))

    #Test the hash functions of Pile objects
    print(hash(d1))
    print(hash(d2))
