#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Examples of usage for of the library
"""

from copy import deepcopy
from model import Faces, Suits, Deck, Pile, Card

def deal_hand():
    """Deal 5 cards from the deck into 3 different hands"""
    d = Deck()
    hands = d.deal(3,5)
    print(hands)

def input_card():
    """Take user input of a card's typeable name, and get the
    relevant card object"""
    while True:
        inp = str(input("Enter the typeable name of a card: "))
        card = Card.get_from_typeable_name(inp)
        if card is not None:
            break
    print(card)

def show_card():
    """Display the string representation of a card"""
    print(Card(Faces.SIX, Suits.SPADES).get_typeable_name())

def make_pile():
    """Create a pile of cards containing the ace of hearts and the
    five of clubs"""
    p = Pile([
        Card(Faces.ACE, Suits.HEARTS),
        Card(Faces.FIVE, Suits.CLUBS),
    ])
    print(p)

def pile_difference():
    """Take the difference of two piles of sets"""
    p1 = Pile([
        Card(Faces.ACE, Suits.HEARTS),
        Card(Faces.FIVE, Suits.CLUBS),
    ])
    p2 = Pile([
        Card(Faces.FIVE, Suits.CLUBS),
    ])
    print(p1 - p2)

def deck_equality():
    """Show two sets of equal contents are equal"""
    d = Deck()
    print(d is deepcopy(d))

def shuffle_and_sort():
    """Create a deck, then shuffle it, then re-sort it"""
    d = Deck()
    print(d)
    d.shuffle()
    print(d)
    d.sort()
    print(d)

def insert_peek_and_pop():
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

if __name__ == "__main__":
    #Run the examples
    deal_hand()
    input_card()
    show_card()
    make_pile()
    pile_difference()
    deck_equality()
    shuffle_and_sort()
    insert_peek_and_pop()
