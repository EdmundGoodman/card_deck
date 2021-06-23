Example Usage
=============

Importing the module
--------------------

.. code-block:: python

    from card_deck import *


Creating and dealing from a deck of cards
-----------------------------------------

.. code-block:: python

    """Deal 5 cards from the deck into 3 different hands"""
    d = Deck()
    hands = d.deal(3,5)
    print(hands)


Taking user input to create a Card object
-----------------------------------------

.. code-block:: python

    """Take user input of a card's typeable name, and get the
    relevant card object"""
    while True:
        inp = str(input("Enter the typeable name of a card: "))
        card = Card.get_from_typeable_name(inp)
        if card is not None:
            break
    print(card)


Display the string representation of a card
-------------------------------------------

.. code-block:: python

    """Display the string representation of a card"""
    print(Card(Faces.SIX, Suits.SPADES).get_typeable_name())


Create a pile of cards
----------------------

.. code-block:: python

    """Create a pile of cards containing the ace of hearts and the
    five of clubs"""
    p = Pile([
        Card(Faces.ACE, Suits.HEARTS),
        Card(Faces.FIVE, Suits.CLUBS),
    ])
    print(p)


Take the difference of two piles of cards
-----------------------------------------

.. code-block:: python

    """Take the difference of two piles of sets"""
    p1 = Pile([
        Card(Faces.ACE, Suits.HEARTS),
        Card(Faces.FIVE, Suits.CLUBS),
    ])
    p2 = Pile([
        Card(Faces.FIVE, Suits.CLUBS),
    ])
    print(p1 - p2)


Show the equality of two similar piles
--------------------------------------

.. code-block:: python

    """Show two sets of equal contents are equal"""
    d = Deck()
    print(d is deepcopy(d))


Create a deck, then shuffle it, then re-sort it
-----------------------------------------------

.. code-block:: python

    """Create a deck, then shuffle it, then re-sort it"""
    d = Deck()
    print(d)
    d.shuffle()
    print(d)
    d.sort()
    print(d)


Peek and pop from the head of a pile of cards
---------------------------------------------

.. code-block:: python

    """Peek and pop from the head of a pile"""
    p1 = Pile([
        Card(Faces.ACE, Suits.HEARTS),
        Card(Faces.FIVE, Suits.CLUBS),
    ])
    print(p1)
    p1.insert(
        Card(Faces.JACK, Suits.SPADES)
    )
    print(p1)
    print(p1.peek())
    print(p1)
    print(p1.pop())
    print(p1)
