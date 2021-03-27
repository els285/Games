# Karma card game (also known as Shithead)

# Defines cards and shuffled list

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit  = suit 


list_suits = ["diamonds","hearts","clubs","spades"]
list_values = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
deck_of_cards = [Card(value,suit) for suit in list_suits for value in list_values]

from random import shuffle
shuffle(deck_of_cards)


# Shithead player class




class Player:


    def Play(self,card2play,played_pile,unused_deck):
        played_pile.append(card2play)
        print("playing " + str(card2play.value))
        if len(unused_deck) > 0:
            self.hand = unused_deck[0]
            unused_deck = unused_deck[1:]
        return played_pile, unused_deck

    def PlayRandom(self,played_pile,unused_deck):

        CanPlay = False
        # First move
        if len(played_pile) == 0:
            played_pile , unused_deck = self.Play(self.hand[0],played_pile,unused_deck)
            return played_pile , unused_deck

        # Define current hand
        if len(self.hand) > 0: 
            self.current_hand = self.hand
        elif len(self.hand) == 0 and len(self.faceup_hand) > 0: 
            self.current_hand = self.faceup_hand

        for card in self.current_hand:
            input_card = played_pile[-1]
            if card.value >= input_card.value:
                CanPlay = True
                played_pile , unused_deck = self.Play(card,played_pile,unused_deck)
                return played_pile , unused_deck
                break 

        if not CanPlay:
            # Pick-up
            print("Can't play; pick up")
            self.hand = self.hand + played_pile
            print(len(self.hand))
            played_pile = []
            return played_pile , unused_deck

        



    def __init__(self):
        self.facedown_hand = []
        self.faceup_hand = []
        self.hand = []

Ethan = Player()
Jess = Player()
Leo = Player()


list_of_players = [Ethan,Jess,Leo]

def Deal(deck_of_cards,list_of_players):

    for player in list_of_players:

        player.facedown_hand = [c for c in deck_of_cards[0:3]]
        player.faceup_hand = [c for c in deck_of_cards[3:6]]
        player.hand = [c for c in deck_of_cards[6:9]]
        deck_of_cards = deck_of_cards[9:]

    return deck_of_cards

# Deal the cards
new_deck_of_cards = Deal(deck_of_cards,list_of_players)

# Play the game

played_pile = []
unused_deck = new_deck_of_cards
x,y=Ethan.PlayRandom(played_pile,unused_deck)
x2,y2 = Jess.PlayRandom(x,y)
x3, y3 = Leo.PlayRandom(x2,y2)




print(len(x3))


