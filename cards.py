#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Provides Card, Pile, and Deck classes for modelling cards, with Suits and
Faces enums as backend data structures

Suits and Faces are enums containing the names and values of their respective
items. Card models a single card, Pile models an ordered list of cards of
arbitrary length, and Deck models a Pile of cards containing every permutation
of suit and face, initially ordered by the enum values.
"""

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
    """An Enum class for the suits in a deck of cards"""
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4

@unique
class Faces(Enum):
    """An Enum class for the faces in a deck of cards"""
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



class Card:
    """A model of a card as having a suit and a face, a printeable and a
    typeable name, and value with respect other cards"""

    def __init__(self, face, suit):
        """Initialise the card as having a face and a suit"""
        self.face = face
        self.suit = suit

    def getFace(self):
        """Get the face of the card"""
        return self.face

    def getSuit(self):
        """Get the suit of the card"""
        return self.suit

    def getTypeableName(self):
        """Get the typeable name of the card, i.e. a unique string to describe
        a card's value.
        The first character of this string represents the face, as either the
        first letter of the face name if it is a picture card, or the number
        of the face if it is not. The second character of this string reprsents
        the suit, as the first letter of the suit name.
        For example, the ace of hearts would be 'AH', whereas the five of clubs
        would be '5C'"""
        faceNum = self.face.value
        suitChar = self.suit.name[0]
        if faceNum in [1,11,12,13]:
            faceChar = self.face.name[0]
        else:
            faceChar = str(faceNum)
        return faceChar + suitChar

    def __eq__(self, other):
        """Return the equality between two cards"""
        return self.face == other.face and self.suit == other.suit

    def __ne__(self, other):
        """Return the inequality between two cards"""
        return self == other

    def __lt__(self, other):
        """Return whether the card has a lower value than another card, first
        by comparing faces, then if they are equal by comparing suits"""
        if self.face < other.face:
            return True
        else:
            return self.suit < other.suit

    def __le__(self, other):
        """Return whether the card has a lower or equal value than another card,
        first by comparing faces, then if they are equal by comparing suits"""
        return self < other or self == other

    def __gt__(self, other):
        """Return whether the card has a greater value than another card, first
        by comparing faces, then if they are equal by comparing suits"""
        if self.face > other.face:
            return True
        else:
            return self.suit > other.suit

    def __ge__(self, other):
        """Return whether the card has a greater or equal value than another card,
        first by comparing faces, then if they are equal by comparing suits"""
        return self > other or self == other

    def __hash__(self):
        """Generate a unique integer representation of the card"""
        return hash(str(self.face.value)+str(self.suit.value))

    def __str__(self):
        """Get a string representing the card, using UTF-8 characters to
        prettily denote the suit"""
        faceChars = "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")
        suitChars = '♦,♣,♥,♠'.split(",")
        return faceChars[self.face.value-1] + suitChars[self.suit.value-1]

    def __repr__(self):
        """Use the string representation of the card as the informal
        representation of the card"""
        return str(self)



class CardFromTypeableName:
    """A utility class to generate a Card object from its typeable name,
    to streamline data entry of cards via a text format"""
    SUIT_LOOKUP = {s.name[0]:s for s in Suits}
    FACE_LOOKUP = {str(f.value):f for f in Faces if f not in [1,10,11,12]}
    #If it's a picture card, use it's first letter to denote it
    FACE_LOOKUP["A"] = Faces.ACE
    FACE_LOOKUP["J"] = Faces.JACK
    FACE_LOOKUP["Q"] = Faces.QUEEN
    FACE_LOOKUP["K"] = Faces.KING

    def getCard(self, typeableName):
        """Return the Card object specified by the typeable name. If the name
        does not reference a valid card, return None"""
        faceChar, suitChar = typeableName[0], typeableName[1]
        face, suit = None, None

        if faceChar in CardFromTypeableName.FACE_LOOKUP:
            face = CardFromTypeableName.FACE_LOOKUP[faceChar]
        if suitChar in CardFromTypeableName.SUIT_LOOKUP:
            suit = CardFromTypeableName.SUIT_LOOKUP[suitChar]

        if len(typeableName) == 2 and face is not None and suit is not None:
            return Card(face, suit)
        else:
            return None



class Pile:
    """A Pile object, which represents an ordered list of cards of arbitrary
    length"""

    def __init__(self, cards=[]):
        """Initialise the pile by default as empty, or with a specified list
        of initial cards"""
        self.cards = cards

    def get(self):
        """Get the list of cards in the pile"""
        return self.cards

    def pop(self, position=None):
        """Pop a card off the pile, by default from the top, or at a specified
        position in the pile"""
        if position is None:
            position = len(self.cards) - 1
        return self.cards.pop()

    def peek(self, position=-1):
        """Peek at the value of a card in the pile, by default the top card, or
        at a specified position in the pile"""
        return self.cards[position]

    def place(self, card, position=None):
        """Place a card into the pile, by default to the top, or at a specified
        position in the pile"""
        if position is None:
            position = len(self.cards)
        self.cards.insert(position, card)

    def shuffle(self):
        """Randomly shuffle the order of the cards in the pile"""
        random.shuffle(self.cards)

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
                    sets[j].place(self.pop())
                except IndexError:
                    return sets
        return sets

    def __add__(self, other):
        """Concatenate a pile to the end of the current pile"""
        return Pile(self.cards.extend(other.cards))

    def __sub__(self, other):
        """Remove all cards from the current pile that are in the other pile
        (take the relative complement of the current and other piles)"""
        return Pile([item for item in self if item not in other])

    def __iter__(self):
        """Create an iterator for the pile of cards"""
        for card in self.cards:
            yield card

    def __contains__(self, item):
        """Return whether the pile contains a specified card"""
        return item in self.get()

    def __len__(self):
        """Get the size of the pile"""
        return len(self.cards)

    def __and__(self, other):
        """Return the intersection of the current and another pile of cards"""
        return Pile([item for item in self.cards if item in other.cards])

    def __or__(self, other):
        """Return the union of the current and another pile of cards"""
        return Pile(list(set(self.cards).union(set(other.cards))))

    def __eq__(self, other):
        """Return whether two piles are equal (i.e. contain the same cards
        in the same order)"""
        return self.cards == other.cards

    def __ne__(self, other):
        """Return whether two piles are not equal (i.e. don't contain the same
        cards in the same order)"""
        return not self == other

    def __hash__(self):
        """Generate a unique integer representation of the pile"""
        return hash("".join([str(hash(x)) for x in self.cards]))

    def __str__(self):
        """Return a string representation of the pile, formatted as a list
        of the string representations of the cards it holds"""
        return ", ".join([str(x) for x in self.cards])

    def __repr__(self):
        """Use the string representation of the pile as the informal
        representation of the pile"""
        return str(self)



class Deck(Pile):
    """A Deck object, which is a Pile object that is initialised with
    every permutation of suit and face, initially ordered by the enum values"""
    def __init__(self):
        Pile.__init__(self)
        for suit in Suits:
            for face in Faces:
                self.cards.append(Card(face, suit))



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
    print(d1)
    print(d2)
    print(d1-d2)
    print(d1 and d3)
    print(d1 is copy.deepcopy(d1))

    #Test the hash functions of Pile objects
    print(hash(d1))
    print(hash(d2))
