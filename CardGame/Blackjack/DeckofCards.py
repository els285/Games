import random

class Card:
    def __init__(self,value,suit):
        self.value          = value
        self.suit           = suit 
        self.num_value      = 0

def generate_deck(shuffle):

    list_suits = ["diamonds","hearts","clubs","spades"]
    list_values = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    deck_of_cards = [Card(value,suit) for suit in list_suits for value in list_values]

    for card in deck_of_cards:
        if card.value in ["2","3","4","5","6","7","8","9","10"]:
            card.num_value = int(card.value) 
        elif card.value in ["Jack","Queen","King"]:
            card.num_value = 10
        else:
            card.num_value = (1,10)

    if shuffle:
        random.shuffle(deck_of_cards)

    return deck_of_cards

