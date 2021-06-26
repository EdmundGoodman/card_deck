#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for the library
"""

import unittest
from model import Faces, Suits, Deck, Pile, Card, CardError, PileError
from copy import deepcopy

class TestCard(unittest.TestCase):
    def test_getters_setters(self):
        """Test that the card object has valid getters and setters"""
        c = Card(Faces.SIX, Suits.HEARTS)
        self.assertEqual(c.face, Faces.SIX)
        self.assertEqual(c.suit, Suits.HEARTS)

        with self.assertRaises(CardError):
            c.face = Faces.SEVEN
        with self.assertRaises(CardError):
            c.suit = Suits.SPADES

    def test_get_from_typeable_name(self):
        """Test that a card can be built from a typeable name"""
        c = Card.get_from_typeable_name("5C")
        d = Card.get_from_typeable_name("10h")
        self.assertIsInstance(c, Card)
        self.assertEqual(c.face, Faces.FIVE)
        self.assertEqual(c.suit, Suits.CLUBS)
        self.assertEqual(d.face, Faces.TEN)
        self.assertEqual(d.suit, Suits.HEARTS)

        with self.assertRaises(CardError):
            Card.get_from_typeable_name("5B")
        with self.assertRaises(CardError):
            Card.get_from_typeable_name("abcd")

    def test_equality(self):
        """Test that cards can be compared for equality"""
        c = Card(Faces.SIX, Suits.HEARTS)
        d = deepcopy(c)
        e = Card(Faces.SEVEN, Suits.CLUBS)
        self.assertEqual(c, d)
        self.assertNotEqual(c,e)

    def test_ordering(self):
        """Test that cards can be compared for equality"""
        c = Card(Faces.SIX, Suits.HEARTS)
        d = Card(Faces.SEVEN, Suits.HEARTS)
        e = Card(Faces.SIX, Suits.SPADES)
        self.assertGreater(d,c)
        self.assertLess(c,d)
        self.assertGreater(d,e)


class TestPile(unittest.TestCase):
    def test_getters_setters(self):
        """Test that the pile object has valid getters and setters"""
        cs = [Card(Faces.ACE, Suits.HEARTS), Card(Faces.FIVE, Suits.CLUBS)]
        p = Pile(deepcopy(cs))
        q = Pile()
        q.cards = cs
        self.assertEqual(p.cards, cs)
        self.assertEqual(p.cards, q.cards)

    def test_peek(self):
        """Test that the pile object has a valid peek operation"""
        cs = [Card(Faces.ACE, Suits.HEARTS), Card(Faces.FIVE, Suits.CLUBS)]
        p = Pile(deepcopy(cs))
        self.assertEqual(p.peek(), cs[-1])
        self.assertEqual(p.peek(0), cs[0])

    def test_pop(self):
        """Test that the pile object has a valid pop operation"""
        cs = [Card(Faces.ACE, Suits.HEARTS), Card(Faces.FIVE, Suits.CLUBS)]
        p = Pile(deepcopy(cs))
        c = p.pop()
        self.assertEqual(c, cs[-1])
        self.assertEqual(len(p.cards), 1)
        with self.assertRaises(PileError):
            Pile().pop()

    def test_insert(self):
        """Test that the pile object has a valid insert operation"""
        cs = [Card(Faces.ACE, Suits.HEARTS)]
        c = Card(Faces.FIVE, Suits.CLUBS)
        p = Pile(deepcopy(cs))
        p.insert(c)
        self.assertEqual(c, p.peek())

    def test_remove(self):
        """Test that the pile object has a valid remove operation"""
        cs = [Card(Faces.ACE, Suits.HEARTS), Card(Faces.FIVE, Suits.CLUBS)]
        p = Pile(deepcopy(cs))
        p.remove(cs[-1])
        self.assertEqual(len(p.cards), 1)
        with self.assertRaises(PileError):
            Pile().remove(Card(Faces.SIX, Suits.HEARTS))

    def test_append_extend(self):
        """Test that the pile object has valid append and extend operations"""
        cs = [Card(Faces.ACE, Suits.HEARTS), Card(Faces.FIVE, Suits.CLUBS)]
        c = Card(Faces.SIX, Suits.HEARTS)
        p = Pile()
        q = Pile(deepcopy(cs))
        p.extend(q)
        self.assertEqual(cs, p.cards)

        cs.append(c)
        p.append(c)
        self.assertEqual(cs, p.cards)

    def test_shuffle_sort(self):
        """Test that the pile object has valid shuffle and sort operations"""
        d = Deck()
        e = deepcopy(d)
        d.shuffle()
        d.sort()
        self.assertEqual(d, e)

    def test_list_forwards(self):
        """Test that list operations on the internal card list are forwarded"""
        cs = [Card(Faces.ACE, Suits.HEARTS), Card(Faces.FIVE, Suits.CLUBS)]
        c = Card(Faces.SIX, Suits.HEARTS)
        p = Pile(deepcopy(cs))
        self.assertTrue(cs[0] in p)
        self.assertTrue(c not in p)

        self.assertEqual(len(cs), len(p))

        self.assertEqual(cs[1], p[1])
        self.assertNotEqual(cs[0], p[1])
        with self.assertRaises(IndexError):
            p[5]

        self.assertEqual(list(iter(cs)), list(iter(p)))

        self.assertEqual(cs[::-1], reversed(p).cards)



if __name__ == "__main__":
    unittest.main()
    print("All tests passed")
