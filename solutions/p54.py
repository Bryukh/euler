# -*- coding: utf-8 -*-
"""
In the card game poker, a hand consists of five cards and are ranked, 
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the 
highest value wins; for example, a pair of eights beats a pair of fives 
(see example 1 below). But if two ranks tie, for example, both players 
have a pair of queens, then highest cards in each hand are compared 
(see example 4 below); if the highest cards tie then the next highest 
cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand        Player 1        Player 2        Winner
1       5H 5C 6S 7S KD
Pair of Fives
    2C 3S 8S 8D TD
Pair of Eights
    Player 2
2       5D 8C 9S JS AC
Highest card Ace
    2C 5C 7D 8S QH
Highest card Queen
    Player 1
3       2D 9C AS AH AC
Three Aces
    3D 6D 7D TD QD
Flush with Diamonds
    Player 2
4       4D 6S 9H QH QC
Pair of Queens
Highest card Nine
    3D 6D 7H QD QS
Pair of Queens
Highest card Seven
    Player 1
5       2H 2D 4C 4D 4S
Full House
With Three Fours
    3C 3D 3S 9S 9D
Full House
with Three Threes
    Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated 
cards), each player's hand is in no specific order, and in each hand there 
is a clear winner.

How many hands does Player 1 win?
"""
__author__ = 'bryukh'

WEIGHT = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
            'T':10, 'J':11, 'Q':12, 'K':13, 'A':14,
            'Pair': 100, 'TPair': 300, 'Three': 500, 'Straight':700,
            'Flush':900, 'FHouse':1100, 'Four':2000, 'SFlush':3000,
            'RFlush':5000}
SUIT = {'C': 1, 'S': 2, 'D': 3, 'H': 4}

class Card(object):
    """Object for card"""

    def __init__(self, sform):
        """init card from string form"""
        self.value = WEIGHT[sform[0]]
        self.suit = SUIT[sform[1]]

    def __repr__(self):
        return str(self.value) + str(self.suit)


class Hand(object):
    """Five card in one hand"""
    cards = set()

    def __init__(self, cards):
        self.cards = set(cards)
        if len(self.cards) != 5:
            raise TypeError

    def values(self):
        """Return list of cards value"""
        return [c.value for c in self.cards]

    def suits(self):
        """Return list of cards suit"""
        return [c.suit for c in self.cards]

    def high_card(self):
        """Return highest card value"""
        return max(self.values())

    def is_same_value(self, quantity):
        """Check cards for same value"""
        values = self.values()
        for check in values:
            if values.count(check) == quantity:
                return check
        return 0

    def is_pair(self):
        """Check cards for pair combination"""
        res = self.is_same_value(2)
        return WEIGHT["Pair"] + res if res else 0

    def is_three(self):
        """Check cards for three combination"""
        res = self.is_same_value(3)
        return WEIGHT["Three"] + res if res else 0

    def is_four(self):
        """Check cards for four combination"""
        res = self.is_same_value(4)
        return WEIGHT["Four"] + res if res else 0

    def is_two_pair(self):
        count_pair = 0
        values = self.values()
        bpair = 0
        lpair = 0
        for check in values:
            if values.count(check) == 2:
                count_pair += 1
                if check > bpair:
                    lpair = bpair
                    bpair = check
                else:
                    lpair = check
        if count_pair == 4:
            return WEIGHT["TPair"] + bpair * 11 + lpair
        return 0

    def is_flush(self):
        return (WEIGHT["Flush"]
                if (self.suits().count(self.suits()[0]) == 5) else 0)

    def is_full_house(self):
        pair = self.is_pair()
        three = self.is_three()
        if pair and three:
            return WEIGHT["FHouse"] + pair + three
        return False

    def is_straight(self):
        svalues = sorted(self.values())
        if [v - svalues[0] for v in svalues] == range(5):
            return WEIGHT["Straight"] + svalues[-1]
        return 0

    def is_straight_flush(self):
        return (WEIGHT["SFlush"] + max(self.values())
                if (self.is_flush() and self.is_straight()) else 0)

    def is_royal_flush(self):
        return (WEIGHT["RFlush"]
                if (self.is_flush() and self.is_straight() and
                    (14 in self.values()))
                else 0)


def get_value(hand):
    return (hand.is_royal_flush() or hand.is_straight_flush() or
            hand.is_four() or hand.is_full_house() or hand.is_flush() or
            hand.is_straight() or hand.is_three() or hand.is_two_pair() or
            hand.is_pair() or hand.high_card())

def solution():
    """
    Bryukh's solution
    >>> solution()
    
    """
    poker = open("eulerfiles/poker54.txt", "r")
    p1_win = 0
    for line in poker.readlines():
        all_cards = line.strip().split()
        p1 = Hand([Card(ch) for ch in all_cards[:5]])
        p2 = Hand([Card(ch) for ch in all_cards[5:]])
        p1_value = get_value(p1)
        p2_value = get_value(p2)
        if p1_value > p2_value:
            p1_win += 1
        elif p1_value == p2_value:
            if sorted(p1.values())[::-1] > sorted(p2.values())[::-1]:
                p1_win += 1
    return p1_win

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)