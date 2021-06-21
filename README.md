Card Deck
=========

An object model of a pack of cards, written in Python, to streamline writing programs to model/play games involving cards

Importing the module
--------------------

``` {python}
from card_deck import card_deck
```

Creating and dealing from a deck of cards
-----------------------------------------

``` {python}
from card_deck import *
d = Deck()
# Deal 5 cards from the deck into 3 different hands
hands = d.deal(3,5)
```

Taking user input to create a Card object
-----------------------------------------

``` {python}
inp = str(input("Enter the typeable name of a card: "))
card = Card.get_from_typeable_name(inp)
print(card)
```

Installation
------------

``` {python}
pip install card-deck
```

Requirements
------------

There are no additional required libraries
