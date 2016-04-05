import random

class Deck(object):
    """ Deck class - deck creation, shuffle, dealing """

    deck = [i for i in range(52)]

    def shuffle(self):
        return random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()
    
    def cardValue(self, card):
        value = card % 13
        if value is 0:
            value = "Ace"
        elif value is 1:
            value = "Jack"
        elif value is 11:
            value = "Queen"
        elif value is 12:
            value = "King"

        suit = card / 13
        if suit is 0:
            suit = " of Spades"
        elif suit is 1:
            suit = " of Hearts"
        elif suit is 2:
            suit = " of Diamonds"
        elif suit is 3:
            suit = " of Clubs"

        return str(value) + suit

    def resetDeck(self):
        self.deck = [i for i in range(52)]


class Player(object):
    """ Player class - hand, score """
    hand = []
    total = 0

    def resetHand(self):
        self.hand = []




def game():
    phase = 0

    while phase is 0:
        
        choice = raw_input("New Blackjack Game?\n Y/n >>")
        
        if choice is 'Y':
            print "Loading game..."
            phase = 1
        elif choice is 'n':
            print "Exiting game..."
            quit(0)

    def createPlayer():
        """ First phase, deal initial hand """
        for i in range(2):
            playerOne.hand.append(currentDeck.deal())


    def calScore(cards):
        pts = 0
        for val in cards:
            pts += score(val)
        return pts

    def score(value):
        if value % 13 is 0:
            return 1
        elif value % 13 is 1:
            return 10
        elif value % 13 > 10:
            return 10
        else:
            return value % 13

    def winCondition():
        if calScore(playerOne.hand) == 21 and phase == 0:
            print "You win!"
            quit(0)
        elif calScore(playerOne.hand) > 21:
            print "Busted!"
            quit(0)

    def action():
        while True:
            choice = raw_input(">> ")
            if choice is 'h' or choice is 'H':
                playerOne.hand.append(currentDeck.deal())
                startUI()
            elif choice is 's' or choice is 'S':
                pass
            elif choice is 'q' or choice is 'Q':
                quit(0)
            else:
                print "Unknown Command"

    def startUI():
        # Display hand UI
        print "-" * 50
        print "Your Hand\n"
        for i in range(len(playerOne.hand)):
            print ">> %s <<" % currentDeck.cardValue(playerOne.hand[i])
        print "-" * 50
        print "Hand Value: %s" % calScore(playerOne.hand)
        winCondition()
        print "(H)Hit -- (S)Stand -- (Q)Quit"
        #Flow to action choice
        action()

    playerOne = Player()
    currentDeck = Deck()
    currentDeck.shuffle()
    createPlayer()
    startUI()

