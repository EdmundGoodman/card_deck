#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provides Card, Pile, and Deck classes for modelling cards, with Suits and
Faces enums as backend data structures

Suits and Faces are enums containing the names and values of their respective
items. Card models a single card, Pile models an ordered list of cards of
arbitrary length, and Deck models a Pile of cards containing every permutation
of suit and face, initially ordered by the enum values.
"""

from enum import Enum, unique

__author__ = "Edmund Goodman"
__copyright__ = "Copyright 2020, Edmund Goodman"
__credits__ = ["Edmund Goodman"]
__license__ = "GPL"
__maintainer__ = "Edmund Goodman"
__email__ = "egoodman3141@gmail.com"


@unique
class Suits(Enum):
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4

@unique
class Faces(Enum):
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
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def getFace(self):
        return self.face

    def getSuit(self):
        return self.suit

    def getTypeableName(self):
        faceNum = self.face.value
        suitChar = self.suit.name[0]
        if faceNum in [1,11,12,13]:
            faceChar = self.face.name[0]
        else:
            faceChar = str(faceNum)
        return faceChar + suitChar

    def __eq__(self, other):
        return self.face == other.face and self.suit == other.suit

    def __ne__(self, other):
        return self == other

    def __lt__(self, other):
        if self.face < other.face:
            return True
        else:
            return self.suit < other.suit

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        if self.face > other.face:
            return True
        else:
            return self.suit > other.suit

    def __ge__(self, other):
        return self > other or self == other

    def __hash__(self):
        return int(str(self.face.value)+str(self.suit.value))

    def __str__(self):
        faceChars = "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")
        suitChars = '♦,♣,♥,♠'.split(",")
        return faceChars[self.face.value-1] + suitChars[self.suit.value-1]

    def __repr__(self):
        return str(self)



class CardFromTypeableName:
    SUIT_LOOKUP = {s.name[0]:s for s in Suits}
    FACE_LOOKUP = {str(f.value):f for f in Faces if f not in [1,10,11,12]}
    #If it's a picture card, use it's first letter to denote it
    FACE_LOOKUP["A"] = Faces.ACE
    FACE_LOOKUP["J"] = Faces.JACK
    FACE_LOOKUP["Q"] = Faces.QUEEN
    FACE_LOOKUP["K"] = Faces.KING

    def getCard(self, typeableName):
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
    def __init__(self, cards=[]):
        self.cards = cards

    def get(self):
        return self.cards

    def pop(self, position=None):
        if position is None:
            position = len(self.cards) - 1
        return self.cards.pop()

    def peek(self, position=-1):
        return self.cards[position]

    def place(self, card, position=None):
        if position is None:
            position = len(self.cards)
        self.cards.insert(position, card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, numSets, numCards):
        sets = [[] for n in range(numSets)]
        for i in range(numCards):
            for j in range(numSets):
                sets[j].append(self.pop())
        return sets

    def __add__(self, other):
        return Pile( self.cards.extend(other.cards) )

    def __sub__(self, other):
        return Pile( [item for item in self if item not in other] )

    def __iter__(self):
        for card in self.cards:
            yield card

    def __contains__(self, item):
        return item in self.get()

    def __len__(self):
        return len(self.cards)

    def __and__(self, other):
        return [item for item in self.cards if item in other.cards]

    def __or__(self, other):
        return list( set(self.cards).union(set(other.cards)) )

    def __eq__(self, other):
        return self.cards == other.cards

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return int("".join([str(hash(x)) for x in self.cards]))

    def __str__(self):
        return ", ".join([str(x) for x in self.cards])

    def __repr__(self):
        return str(self)



class Deck(Pile):
    def __init__(self):
        Pile.__init__(self)
        for suit in Suits:
            for face in Faces:
                self.cards.append(Card(face, suit))



if __name__=="__main__":
    """Test the interfaces of the objects"""
    import copy

    print(Card(Faces.SIX, Suits.SPADES).getTypeableName())


    while True:
        inp = str(input("Enter the typeable name of a card: "))
        card = CardFromTypeableName().getCard(inp)
        if card is not None:
            break
    print(card)


    d1 = Deck()
    d2 = Pile([Card(Faces.ACE, Suits.DIAMONDS)])
    d3 = Pile([
        Card(Faces.ACE, Suits.HEARTS),
        Card(Faces.FIVE, Suits.CLUBS),
    ])

    print(d1)
    print(d2)
    print(d1-d2)
    print(d1 and d3)
    print(d1 is copy.deepcopy(d1))
    print(hash(d1))
    print(hash(d2))
