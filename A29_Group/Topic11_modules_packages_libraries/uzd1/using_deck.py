# now we can use our deck
import deck # could also do from deck import Deck

my_deck = deck.Deck()
print(my_deck.peek(5))
print(my_deck.shuffle().peek(5))
# deal 5 cards
my_cards = my_deck.deal(5)
print(my_cards)
# now peek again
print(my_deck.peek(5)) # so those would be dealt next