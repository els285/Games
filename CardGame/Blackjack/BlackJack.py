from DeckofCards import generate_deck

splitDictionary = {}


softDictionary = {}




# def perfect_strategy()



class Player:

    def __init__(self,name,position,initial_pot):
        self.name     = name
        self.position = position

        # Round-specific attributes
        self.hand = [None,None]
        self.pot  = initial_pot
        self.total = self.compute_total()


    def bet(self,bet):
        self.betted_amount = bet 
        self.pot = self.pot - bet


    def update_pot(self):
        pass


    def compute_total(self):
        return self.hand[0].num_value + self.hand[1].num_value


    def stick_of_twist(self):

        # Is it soft, split or normal
        if self.hand[0].value == self.hand[1].value:
            # Consider whether to split
            pass
        elif self.hand[0].value=="Ace" or self.hand[1].value=="Ace":
            # consider whether to 
            pass
        else:
            pass
        

        # Switch for choosing play



class Dealer:

    def __init__(self):
        self.hand = [None,None]
        self.face_up_card   = self.hand[0] 
        self.face_down_card = self.hand[1]




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


    def initial_deal(self):

        for i in range(0,2):
            for Participant in  self.players + [self.dealer]:
                Participant.hand[i] = self.deck[0]
                self.deck = self.deck[1:]   
        

Game1 = Game(num_decks=6,num_players=4)

Game1.initial_deal()

print(Game1.players[0].compute_total())
