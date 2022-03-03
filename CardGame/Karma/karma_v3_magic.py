# Karma card game (also known as Shithead)

import random

# Defines cards and shuffled list

class Card:
    def __init__(self,value,suit,num_value):
        self.value          = value
        self.suit           = suit 
        self.num_value      = num_value
        self.magic          = False

def GenerateDeck():

    list_suits = ["diamonds","hearts","clubs","spades"]
    list_values = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    list_num_values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    deck_of_cards = [Card(value,suit,num_value) for suit in list_suits for (value,num_value) in zip(list_values,list_num_values)]

    random.shuffle(deck_of_cards)

    return deck_of_cards


def GenerateMagicDeck():

    list_suits = ["diamonds","hearts","clubs","spades"]
    list_values = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    list_num_values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    deck_of_cards = [Card(value,suit,num_value) for suit in list_suits for (value,num_value) in zip(list_values,list_num_values)]

    for c in deck_of_cards:
        if c.num_value == 2 or c.num_value == 3 or c.num_value == 10:
            c.magic = True

    random.shuffle(deck_of_cards)

    return deck_of_cards


def PrintCards(list_of_card_objects):
    for c in list_of_card_objects:
        print(c.value,c.suit)



# Shithead player class

class Player:


    def Play(self,card2play,played_pile,unused_deck):

        # Play the card
        print(card2play)
        played_pile.append(card2play)
        self.temp_hand.remove(card2play)
        print("playing " + str(card2play.value) + " (of " + str(card2play.suit) + ")")

        # Apply some rules
        if card2play.num_value == 10:
            played_pile = []

        if len(played_pile) >= 4:
            if card2play.num_value == played_pile[-2].num_value and card2play.num_value == played_pile[-3].num_value and card2play.num_value == played_pile[-4].num_value:
                played_pile = []

        # Pick-up if player has less than 3 cards and there are still unused cards left
        if self.status == "inhand":
            self.current_hand = self.temp_hand
            if len(unused_deck) > 0 and len(self.temp_hand) < 3:
                self.current_hand.append(unused_deck[0])
                unused_deck = unused_deck[1:]

        elif self.status == "faceup":
            self.faceup_hand = self.temp_hand
            self.current_hand = []

        elif self.status == "facedown":
            self.current_hand = []
            self.facedown_hand = [c for c in self.facedown_hand if c != card2play]

        return played_pile, unused_deck 

    def CantPlay(self,played_pile):
        print("Can't play; pick up")

        # If player still has cards in hand, player_pile is added to these
        if self.status == "inhand":
            self.current_hand = self.temp_hand + played_pile

        # Point of contention here - if you can't play from faceup, do you pick one of them up?
        # If player is on face-up and can't play, only the played_cards become the hand
        elif self.status == "faceup":
            self.current_hand = played_pile

        elif self.status == "facedown":
            self.current_hand = self.temp_hand + played_pile 

        print("Picked up hand is")
        played_pile = []

        return played_pile


    def SelectBest(self,current_hand,input_card_value):
        playable_hand = [c for c in current_hand if c.num_value >= input_card_value]
        if len(playable_hand) > 0:
            sorted_hand = sorted(playable_hand, key=lambda x: x.num_value, reverse=False)
            return sorted_hand[0]
        elif len(playable_hand) == 0:
            return None

    
    def SelectBestMagic(self,current_hand,input_card_value):

        # Also need to validate particular cards
        if input_card_value == 7:
            playable_hand = [c for c in current_hand if c.num_value <= input_card_value]
        else:
            playable_hand = [c for c in current_hand if c.num_value >= input_card_value]

        magic_hand    = [c for c in current_hand if c.magic == True]
        # First use non-magic cards
        if len(playable_hand) > 0:
            sorted_hand = sorted(playable_hand, key=lambda x: x.num_value, reverse=False)
            return sorted_hand[0]
        elif len(playable_hand) == 0 and len(magic_hand) > 0:
            sorted_magic_hand = sorted(magic_hand,    key=lambda x: x.num_value, reverse=False)
            print("magic hand utilised")
            print(magic_hand)
            return sorted_magic_hand[0]
        elif len(playable_hand) == 0:
            return None


        
    def ExecuteMagic(self,played_pile,unused_deck):

        
        # if self.status == "facedown":
        #     print(self.temp_hand)
        #     input()

        
        # If played_pile empty, any card can be played
        if len(played_pile) == 0:
            input_card_value = 1
            card2play = self.SelectBestMagic(self.temp_hand,input_card_value)
            played_pile , unused_deck = self.Play(card2play,played_pile,unused_deck)

            # if self.status == "facedown":
            #     print(card2play)
            #     print(self.temp_hand)
            #     print(self.current_hand)
            #     print(self.faceup_hand)
            #     print(self.facedown_hand)
            #     input()

        # If played_pile not empty, card must meet requirement
        elif len(played_pile) > 0:

            # Check for a 3
            if played_pile[-1].num_value == 3 and len(played_pile) >=2:
                input_card_value = played_pile[-2].num_value
            else:
                input_card_value = played_pile[-1].num_value

            # Select best card to play - this is the lowest card which is compatible
            card2play = self.SelectBestMagic(self.temp_hand,input_card_value)

            # It no compatible cards, execute CantPlay
            if card2play == None:
                played_pile = self.CantPlay(played_pile)

            # If a card is compatible, execite Play
            else:
                played_pile , unused_deck = self.Play(card2play,played_pile,unused_deck)


            
            # if self.status == "facedown":
            #     print(card2play)
            #     print(self.temp_hand)
            #     print(self.current_hand)
            #     print(self.faceup_hand)
            #     print(self.facedown_hand)
            #     input()

        return played_pile,unused_deck

    
    def Execute(self,played_pile,unused_deck):

        
        # if self.status == "facedown":
        #     print(self.temp_hand)
        #     input()

        
        # If played_pile empty, any card can be played
        if len(played_pile) == 0:
            input_card_value = 1
            card2play = self.SelectBest(self.temp_hand,input_card_value)
            played_pile , unused_deck = self.Play(card2play,played_pile,unused_deck)

            # if self.status == "facedown":
            #     print(card2play)
            #     print(self.temp_hand)
            #     print(self.current_hand)
            #     print(self.faceup_hand)
            #     print(self.facedown_hand)
            #     input()

        # If played_pile not empty, card must meet requirement
        elif len(played_pile) > 0:
            input_card_value = played_pile[-1].num_value

            # Select best card to play - this is the lowest card which is compatible
            card2play = self.SelectBest(self.temp_hand,input_card_value)

            # It no compatible cards, execute CantPlay
            if card2play == None:
                played_pile = self.CantPlay(played_pile)

            # If a card is compatible, execite Play
            else:
                played_pile , unused_deck = self.Play(card2play,played_pile,unused_deck)


            
            # if self.status == "facedown":
            #     print(card2play)
            #     print(self.temp_hand)
            #     print(self.current_hand)
            #     print(self.faceup_hand)
            #     print(self.facedown_hand)
            #     input()

        return played_pile,unused_deck

            

    def PlayLowest(self,played_pile,unused_deck):

        if len(self.current_hand) != 0:
            # print("option inhand")
            self.status = "inhand"
            self.temp_hand = self.current_hand
            played_pile,unused_deck = self.Execute(played_pile,unused_deck)

        elif len(self.current_hand)==0 and len(self.faceup_hand) != 0:
            # This means that all in-hand cards have been played
            # Therefore construct new hand
            print("option faceup")
            self.status = "faceup"
            self.temp_hand = self.faceup_hand
            played_pile,unused_deck = self.Execute(played_pile,unused_deck)

        elif len(self.current_hand) == 0 and len(self.faceup_hand) == 0 and len(self.facedown_hand) != 0:
            print("option facedown")
            # input()
            self.status = "facedown"
            self.temp_hand = [random.choice(self.facedown_hand)]
            played_pile,unused_deck = self.Execute(played_pile,unused_deck)


    def PlayMagic(self,played_pile,unused_deck):

        if len(self.current_hand) != 0:
            # print("option inhand")
            self.status = "inhand"
            self.temp_hand = self.current_hand
            played_pile,unused_deck = self.ExecuteMagic(played_pile,unused_deck)

        elif len(self.current_hand)==0 and len(self.faceup_hand) != 0:
            # This means that all in-hand cards have been played
            # Therefore construct new hand
            print("option faceup")
            self.status = "faceup"
            self.temp_hand = self.faceup_hand
            played_pile,unused_deck = self.ExecuteMagic(played_pile,unused_deck)

        elif len(self.current_hand) == 0 and len(self.faceup_hand) == 0 and len(self.facedown_hand) != 0:
            print("option facedown")
            # input()
            self.status = "facedown"
            self.temp_hand = [random.choice(self.facedown_hand)]
            played_pile,unused_deck = self.ExecuteMagic(played_pile,unused_deck)



        return played_pile , unused_deck

        
    def __init__(self,name):
        self.name           = name
        self.facedown_hand  = []
        self.faceup_hand    = []
        self.initial_hand   = []
        self.current_hand   = []
        self.status         = "inhand"


def Karma_Deal(deck_of_cards,list_of_players):

    for player in list_of_players:

        player.facedown_hand    = [c for c in deck_of_cards[0:3]]
        player.faceup_hand      = [c for c in deck_of_cards[3:6]]
        player.initial_hand     = [c for c in deck_of_cards[6:9]]
        deck_of_cards           = deck_of_cards[9:]

    return deck_of_cards

Ethan = Player("Ethan")
Jess  = Player("Jess")
Leo   = Player("Leo")
Garry = Player("Garry")


list_of_players = [Ethan,Jess,Leo,Garry]

class Game:

    def __init__(self,list_of_players):
        
        # Given list of players, generates fresh deck of shuffled cards and assigns to each person

        self.list_of_players = list_of_players

        self.deck = GenerateMagicDeck()

        self.remaining_deck = Karma_Deal(self.deck,self.list_of_players)

        self.played_pile = []

    
    def GamePlay(self):


        GameWon = False

        # Set players current_hand. current_hand is the dynamic object
        for player in self.list_of_players:
            player.current_hand = player.initial_hand


        while not GameWon:
            for player in self.list_of_players:
                print(str(player.name) + " playing...")

                self.played_pile,self.remaining_deck = player.PlayMagic(self.played_pile,self.remaining_deck)

                print(self.played_pile)
                print(player.current_hand)
                input()


                if len(player.facedown_hand) == 0:
                    print("WE HAVE A WINNER")
                    GameWon = True
                    Winner  = player
                    break

            print("\n")
            # input()

        print("The winner is " + Winner.name)
        exit()
            

def main():

    Game1 = Game(list_of_players)

    Game1.GamePlay()

main()
    



