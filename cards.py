from enum import Enum, unique

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


class CardFromTypeableName:
    SUIT_LOOKUP = {s.name[0]:s for s in Suits}
    FACE_LOOKUP = {str(f.value):f for f in Faces if f not in [1,10,11,12]}
    FACE_LOOKUP["A"] = Faces.ACE
    FACE_LOOKUP["J"] = Faces.JACK
    FACE_LOOKUP["Q"] = Faces.QUEEN
    FACE_LOOKUP["K"] = Faces.KING

    def __init__(self, typeableName):
        face = CardFromLetter.FACE_LOOKUP[typeableName[0]]
        suit = CardFromLetter.SUIT_LOOKUP[typeableName[1]]
        card = Card(suit, face)
        self.__class__ = card.__class__
        self.__dict__ = card.__dict__



class Card:
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def getSuit(self):
        return self.suit

    def getFace(self):
        return self.face

    def getTypeableName(self):
        suitChar = self.suit.name[0]
        faceNum = self.face.value
        #If it's a picture card, use it's first letter to denote it
        if faceNum in [1,11,12,13]:
            faceChar = self.face.name[0]
        else:
            faceChar = str(faceNum)
        return faceChar + suitChar

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
                self.cards.append(Card(suit, face))



if __name__=="__main__":
    """Test the interfaces of the objects"""
    import copy

    print(Card(Suits.SPADES, Faces.SIX).getTypeableName())

    #while True:
    #    inp = str(input("Enter the typeable name of a card: "))
    print(type(CardFromLetter("AH")))


    d1 = Deck()
    d2 = Pile([Card(Suits.DIAMONDS, Faces.ACE)])
    d3 = Pile([
        Card(Suits.HEARTS, Faces.ACE),
        Card(Suits.CLUBS, Faces.FIVE),
    ])

    print(d1)
    print(d2)
    print(d1-d2)
    print(d1 and d3)
    print(d1 is copy.deepcopy(d1))
    print(hash(d1))
    print(hash(d2))
