# let's make a function that returns a deck of shuffled cards
# cards have suits and ranks
# suits are ♦, ♣, ♥, ♠
# ranks are 2,3,4,5,6,7,8,9,10,J,Q,K,A

# usually imports go up top

import random

# we will pass in default values for suits and ranks
def get_deck(suits="♦♣♥♠", ranks="234567891JQKA"):
    # we will use list comprehension to generate all possible cards
    # we will use nested loops to iterate over suits and ranks
    return [rank+suit for suit in suits for rank in ranks] # double list comprehension
# instead we could use list(itertools.product(suits, ranks)) # itertools.product generates all possible combinations

# # let's test our function
# deck = get_deck()
# print(deck)
# print(f"Deck has {len(deck)} cards")


def get_shuffled_deck(suits="♦♣♥♠", ranks="234567891JQKA"):
    deck = get_deck(suits, ranks)
    random.shuffle(deck) # IN PLACE shuffle modifies the list
    return deck

# shuffled_deck = get_shuffled_deck()
# print(shuffled_deck)

# let's make a class Deck that implements these functions as methods

class Deck:
    def __init__(self, suits="♦♣♥♠", ranks=tuple("23456789JQKA")+("10",)):
        # again for default values we use immutable objects
        # such as strings, numbers, tuples, NOT lists NOT dictionaries
        self.suits = suits
        self.ranks = ranks
        self.cards = self._gen_deck() # we will generate deck in constructor
        # could add shuffle here if we wanted to

    # let's make a gen_deck method that generates a deck
    def _gen_deck(self):
        # return [rank+suit for suit in self.suits for rank in self.ranks]
        # let's use itertools.product to generate all possible combinations
        import itertools # you can import inside a method
        return list(itertools.product(self.ranks, self.suits)) # list of tuples
    
    def get_deck(self):
        return self.cards
    
    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards # we do not have to return the deck but it is useful for testing
    
    # let's make a deal methods
    def deal(self, n=1):
        # we will deal n cards from the top of the deck
        # we will return a list of n cards
        # we will remove these cards from the deck
        dealt = self.cards[:n] # slice n cards
        self.cards = self.cards[n:] # remove n cards from the deck
        return dealt
    

# let's test our class
# let's use main guard
if __name__ == "__main__":
    # let's test our class
    deck = Deck()
    print(deck.get_deck())
    deal_5 = deck.deal(5)
    print(deal_5)
    # instead lets get another deck with shuffled cards
    new_deck = Deck()
    # print unshuffled deck
    print(new_deck.get_deck())
    new_deck.shuffle_deck()
    deal_3 = new_deck.deal(3)
    print(deal_3)


# for now individual cards are tuples
# instead you could have made them objects from Card class but no need in this case