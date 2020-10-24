import enum


class Suits(enum.Enum):
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3
    SPADES = 4


class Faces(enum.Enum):
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
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def getSuit(self):
        return self.suit

    def getFace(self):
        return self.face

    def __eq__(self, other):
        return self.suit == other.suit and self.face == other.face

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
        return int(str(self.suit.value)+str(self.face.value))

    def __str__(self):
        faceChars = "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")
        suitChars = '♦,♣,♥,♠'.split(",")
        return faceChars[self.face.value-1] + suitChars[self.suit.value-1]

    def __repr__(self):
        return str(self)
