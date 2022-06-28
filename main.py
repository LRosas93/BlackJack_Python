from random import shuffle

class Card:

    faceCards = ["Jack", "King", "Queen"]
    card_fails = []

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

        if value in Card.faceCards:
            self.card_value = 10
        else:
            # drawing an Ace card raises a ValueError
            try:
                self.card_value = int(value)
            except ValueError:
                self.card_value = None

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    deck = []
    suits = ["Diamonds", "Hearts", "Spades", "Clovers"]
    values = ["2", "3", "4",
              "5", "6", "7",
              "8", "9", "10",
              "Ace", "Jack", "Queen", "King"]

    def __init__(self):
        for suit in Deck.suits:
            for value in Deck.values:
                self.deck.append(Card(suit, value))
        shuffle(self.deck)


    def remove_card(self):
        return self.deck.pop()


class Dealer:
    score_value = 0
    rounds_won = 0
    hand = []


    def __init__(self, name="Dealer"):
        self.name = name


    def recieve_card(self, card):
        """takes card objects as param"""
        self.hand.append(card)
        self.addScore_count(card)


    def addScore_count(self, card):
        if card.value == "Ace":
            if self.score_value <= 10:
                self.card_value = 11
            elif self.score_value <= 20:
                self.card_value = 1
        else:
            self.score_value += card.card_value


    def display_score(self):
        # score of the first card drawn
        first_card = self.hand[0]
        print(f"Dealer has a score of: {first_card.card_value}")


    # returns a boolean to see if dealer should deal another card
    def isDraw_card(self):
        if self.score_value <= 17:
            return True
        return False



class Player(Dealer):
    pass


class Game:

    def main(self):
        self.dealer = Dealer()
        self.player = Player("TestUser")
        self.deck = Deck()
        self.test_rounds = 3 # perform test rounds

        for i in range(self.test_rounds):
            self.restart_game()
            self.deal_cards(self.dealer)
            print("=" * 20, "\n")
            self.deal_cards(self.player)
            print("=" * 20, "\n")
            bust = False

            # when player is dealt BlackJack at starting hand
            if self.player.score_value == 21:
                print("BlackJack!\nCongratulations!!")
                self.restart_game()
                continue

            while not bust:

                self.display_currentScore()
                print("'HIT' or 'STAY?'")
                response = input("").upper()

                #  player draws until busts, stay, or hits blackJack
                if response == "HIT":
                    card = self.deck.remove_card()
                    self.player.recieve_card(card)
                    print(f"{self.player.name}" + " drew", card)

                elif response == "STAY":

                    # dealer draws until bust or score is <= 17
                    isDealer_nextCard = self.dealer.isDraw_card()
                    print("Dealer's hand:")
                    while isDealer_nextCard:
                        for card in self.dealer.hand:
                            print(card, end="|")
                        card = self.deck.remove_card()
                        self.dealer.recieve_card(card)
                        print("dealer" + " drew", card, end="\n") # this could be in a method of its own
                        isDealer_nextCard = self.dealer.isDraw_card()

                    if self.dealer.score_value > 21:
                            self.display_finalScore()
                            print("You win this round!")
                            print("=" * 20, "\n")
                            break

                    # this is called after dealer hits busts, or stays
                    isPlayer_winner = self.isWinner()
                    if isPlayer_winner:
                        self.display_finalScore()
                        print("You win this round!")
                        print("=" * 20, "\n")
                        break
                    else:
                        self.display_finalScore()
                        print("Better luck next time!")
                        print("=" * 20, "\n")
                        break


                blackJack = self.isBlackJack()
                # doesn't run unless it's a blackjack for player
                if blackJack:
                    print("BlackJack!\nCongratulations!!")
                    break

                # display current score
                self.display_currentScore() # Buggy code
                bust = self.isBust()

            if bust:
                print("Busts\nBetter luck next time!")
                print("=" * 20, "\n")


    # this method is ccalled at the starting point of cards dealt, (the starting hand)
    def deal_cards(self, card_reciever): # buggy code
            for i in range(2):
                card = self.deck.remove_card()
                card_reciever.recieve_card(card)

                if card_reciever is self.player:
                    print(f"{self.player.name} drew {card}")
                # this is the dealer's starting hand: sccore_value is unknown
                elif card_reciever is self.dealer and len(self.dealer.hand) < 2:
                    print(f"Dealer drew {card_reciever.hand[0]}")


    def isBust(self):
        if self.player.score_value > 21:
            return True
        return False


    # should be called at the end of round,
    def isWinner(self):
        player_score = self.player.score_value
        dealer_score = self.dealer.score_value
        if player_score > dealer_score:
            return True
        return False


    def isBlackJack(self):
        if self.player.score_value == 21:
            return True
        return False


    def display_finalScore(self):
        print(f"{self.player.name} has a score of: {self.player.score_value}")
        print(f"{self.dealer.name} has a score of: {self.dealer.score_value}")


    def display_currentScore(self):
        print(f"{self.player.name} has a score of: {self.player.score_value}")
        self.dealer.display_score()


    # You have to restart the game after end result of comparison
    def restart_game(self):
        self.player.hand = []
        self.dealer.hand = []
        self.player.score_value = 0
        self.dealer.score_value = 0
        self.bust = False


game = Game()
game.main()
