from DeckofCards import generate_deck

from perfect_strategy_generator import standard_Strategy 



def stick_or_twist(player,dealer):
    # For simplest example only
    player_hand = player.hand
    p0,p1 = player_hand[0].num_value,player_hand[1].num_value
    total = p0+p1
    strat = standard_Strategy[(total,dealer.face_up_card.num_value)]
    return strat

class Player:

    def __init__(self,name,position,initial_pot):
        self.name     = name
        self.position = position

        # Round-specific attributes
        self.hand = []
        self.pot  = initial_pot
        # self.total = self.compute_total()
        self.status = None
        self.betted_amount = 0


    def bet(self,bet):
        self.betted_amount += bet 
        self.pot = self.pot - bet


    def receive_winnings(self,winnings):
        self.betted_amount = 0
        self.pot += winnings


    # def compute_total(self):
    #     return self.hand[0].num_value + self.hand[1].num_value


    # def make_choice(self,dealer):
    #     strat = stick_or_twist(self.hand,dealer=dealer)
    #     if strat=="S":
    #         pass 
    #     elif strat="H":
    #         pass
    #         # Get a card



    # def stick_of_twist(self):

    #     # Is it soft, split or normal
    #     if self.hand[0].value == self.hand[1].value:
    #         # Consider whether to split
    #         pass
    #     elif self.hand[0].value=="Ace" or self.hand[1].value=="Ace":
    #         # consider whether to 
    #         pass
    #     else:
    #         pass
        

        # Switch for choosing play



class Dealer:

    def __init__(self):
        self.hand = []
        self.face_up_card   = None 
        self.face_down_card = None




class Game:


    def generate_players(self):
        #Pot set to 10 each
        self.players = [Player("Player"+str(p) , p , 10) for p in range(0,self.num_players)]


    def __init__(self,num_decks,num_players):
        self.num_decks   = num_decks
        self.num_players = num_players
        self.deck = []
        self.generate_players()
        self.dealer = Dealer()

        # Generate the shuffled deck of cards
        for i in range(0,self.num_decks):
            i_deck = generate_deck(True)
            for c in i_deck:
                self.deck.append(c)

        self.og_deck = self.deck


    def initial_deal(self):

        for i in range(0,2):
            for Participant in  self.players + [self.dealer]:
                self.deal_to_participant(Participant)
        self.dealer.face_up_card = self.dealer.hand[0]
        self.dealer.face_down_card = self.dealer.hand[1]

    def initial_bets(self,betting_amount):

        """
        Here, all players bet the same amount. This should become a method of the Player class such that a betting strategy can be implemented
        """

        for player in self.players:
            player.bet(betting_amount)

    def deal_to_participant(self,player):

        player.hand.append(self.deck[0])
        self.deck = self.deck[1:]
        

    def play_round(self):
        # Deal the cards
        self.initial_deal()

        for player in self.players:
            # Compute initial strategy
            strat = stick_or_twist(player,self.dealer)

            # print(self.dealer.face_up_card.value)
            # print(player.hand[0].__dict__)
            # print(player.hand[1].__dict__)
            # print(strat)
            # input()

            # Whilst still hitting, deal another card and re-evaluate strategy
            while strat=="H":
                self.deal_to_participant(player)
                strat = stick_or_twist(player,self.dealer)

            if strat=="D":
                # self.bet_double()
                self.deal_to_participant(player)
                strat = stick_or_twist(player,self.dealer)


            # At this point, the strat should always equal"S"
            print(strat)
            input()

            # Eventually
            if player.total>21:
                player.status = "BUST"
            elif player.total <=21:
                if player.total > self.dealer.total:
                    player.status="WIN"
                    player.receive_winnings(2*player.bet)
                elif player.total < self.dealer.total:
                    player.status="BUST"
                else:
                    player.status="DRAW"

            



Game1 = Game(num_decks=6,num_players=4)

Game1.play_round()

# Game1.initial_deal()


# stick_or_twist(Game1.players[0].hand,Game1.dealer)

# print(Game1.players[0].compute_total())
