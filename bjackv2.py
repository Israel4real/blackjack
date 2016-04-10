import random

class Deck(object):
    """ Deck class - deck creation, shuffle, dealing """
    def __init__(self):
        self.cards = [Card(i) for i in range(52)]

    def shuffle(self):
        return random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()

    def list(self):
        for i in self.cards:
            print i.card_name()

    def reset_deck(self):
        self.cards = [Card(i) for i in range(52)]

class Card(object):
    """ Holds card face/value and suit """
    def __init__(self, id_number):
        self.id_number = id_number
        self.face = id_number % 13
        self.suit = id_number / 13

    def card_name(self):
        """ Returns the card's name """
        face, suit = self.face, " err suit"
        if self.face == 0:
            face = "Ace"
        elif self.face == 1:
            face = "Jack"
        elif self.face == 11:
            face = "Queen"
        elif self.face == 12:
            face = "King"

        if self.suit == 0:
            suit = " of Spades"
        elif self.suit == 1:
            suit = " of Hearts"
        elif self.suit == 2:
            suit = " of Diamonds"
        elif self.suit == 3:
            suit = " of Clubs"

        return str(face) + suit

    def card_value(self):
        face_values = {0: 1, 1: 10, 11: 10, 12: 10}
        if self.face in face_values:
            return face_values[self.face]
        else:
            return self.face


class Hand(object):
    """ Holds cards and card values """
    def __init__(self):
        self.holding = []
        self.total_pts = 0

    def draw(self, drawn_card):
        self.holding.append(drawn_card)
        if drawn_card.face == 0 and self.total_pts < 11:
            self.total_pts += 11
        else:
            self.total_pts += drawn_card.card_value()

    def list_cards(self):
        for card in self.holding:
            print card.card_name()

    def reset_player(self):
        self.holding = []
        self.total_pts = 0

class Player(object):
    """Player class - name, credits, hand"""
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.hand = Hand()

    def hit_or_stand(self):
        pass

class Dealer(Player):
    pass

class Game(object):
    """ Takes player and deck, initializes game"""
    def __init__(self, player):
        self.player = Player(player, 500)
        self.deck = Deck()
        self.phase = 0

    def display(self):
        print "-" * 50
        print " \n" * 5
        print self.player.name
        self.player.hand.list_cards()
        print "\n Current Score:", self.player.hand.total_pts
        print "-" * 50
        print "   --- (H)Hit -- (S)Stand -- (Q)Quit ---"

    def play(self):
        self.deck.shuffle()
        self.player.hand.draw(self.deck.deal())
        self.player.hand.draw(self.deck.deal())
        self.display()

testengine = Game("Koko Yoko")
testengine.play()

# testengine.player.hand.draw(testengine.deck.deal())
# print testengine.player.hand.holding[0].id_number
# testengine.player.hand.list_cards()
# testengine.deck.list()
