Card Deck
=========

An object model of a pack of cards, written in Python, to streamline writing programs to model/play games involving cards


Documentation
-------------

Documentation for the library can be found here: [https://card-deck.readthedocs.io/en/latest/](https://card-deck.readthedocs.io/en/latest/)

Installation
------------

The library has been published on PyPi, so can be found here: [https://pypi.org/project/card-deck/](https://pypi.org/project/card-deck/), and and can be installed as follows:

``` {python}
pip install card-deck
```

Requirements
------------

There are no additional required libraries

Importing the module
--------------------

``` {python}
from card_deck import *
```

Creating and dealing from a deck of cards
-----------------------------------------

``` {python}
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

