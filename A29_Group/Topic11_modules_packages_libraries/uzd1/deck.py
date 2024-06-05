# let's make a card deck class
# we will have an option to shuffle
# we will have an option to deal n cards from the top
import itertools
import random

class Deck:
    def __init__(self, 
                 vertibas = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
                 , masts = '♠♣♥♦'):


        # self.vertibas = vertibas # we do not really need them as we will be creating our deck

        self.kava = list(itertools.product(vertibas, masts))
        # for more complex decks we could creat list of Card objects
        # of course defining Card class first and then using it
        print("New unsorted deck created")


    def shuffle(self):
        random.shuffle(self.kava)
        return self # could also return self.kava

    def deal(self, n):
        dealt_cards = self.kava[:n]
        self.kava = self.kava[n:] 
        return dealt_cards
    
    def peek(self, n):
        return self.kava[:n] # does not change the deck