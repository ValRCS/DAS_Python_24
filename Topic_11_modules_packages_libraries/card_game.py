# we can import Deck from cards module
from cards import Deck

# now I can make a card game
# let's make a simple blackjack game
# we will need a deck of cards
# we will need a player

# for now let's make a while loop that deals cards to the player
# and shows the player's hand
# and asks if it wants to continue

# for now we will store current score in a variable
# init
score = 0
deck = Deck()
deck.shuffle_deck()

while score < 21: # would be good to have 21 as a constant

    card = deck.deal()[0] # deal returns a list of cards, we take the first one
    # by default we deal 1 card anyways
    print(card)
    rank, suit = card
    if rank in "JQK":
        score += 10
    elif rank == "A":
        score += 11
    else:
        score += int(rank)
    print(f"Current score: {score}")
    if score == 21:
        print("Blackjack!")
        break
    elif score > 21:
        print("Bust!")
        break
    else:
        choice = input("Do you want another card? (y/n)")
        if choice.lower() != "y":
            break

# TODO add dealer code
# then you have PvC game Player vs Computer