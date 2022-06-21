from random import shuffle
# Card Values: It is up to player if an ace is worth 1 or 11.
# Face cards are 10 and any other card is its absolute value.

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + " of " + self.suit

class Deck:
    deck = []
    faceCards = ["Jack", "King", "Queen"]
    intValues = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    suits = ["Diamond", "Heart", "Spades", "Clover"]
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

class Player():
    score_value = 0
    rounds_won = 0
    hand = []

    def __init__(self, name="TestUser"):
        self.name = name


    def recieve_card(self, card):
        self.hand.append(card)
        print(self.name + " drew", card)
        self.addScore_count(card)


    def addScore_count(self, card):
        if card.value in Deck.intValues:
            self.score_value += int(card.value)
        elif card.value in Deck.faceCards:
            self.score_value += 10
        elif card.value == "Ace":
            print("You drew an Ace of", card.suit)
            print("Do you want it to be worth '1' or '11'")
            self.score_value += int(input(""))

    def printHand(self):
        for card in self.hand:
            print(card)


# to work sequentially, first call the main()
class Game:

    # all the game logic goes here
    def main(self):
        self.player = Player()
        self.deck = Deck()
        self.deal_cards()
        while self.player.score_value <= 21:
            if self.player.score_value == 21:
                print(isWinner())
                break
            print(f"You have a score of {self.player.score_value}")
            print("'HIT' or 'STAY?'\n")
            response = input("")
            if response == "HIT":
                self.card = self.deck.remove_card()
                self.player.recieve_card(self.card)
                print(self.player.score_value)
            else:
                print(self.player.score_value)
                isWinner = self.isWinner()
                print(isWinner)
                break


    def deal_cards(self):
        for i in range(2):
            card = self.deck.remove_card()
            self.player.recieve_card(card)


    def isWinner(self):
        if self.player.score_value == 21:
            return "BlackJack!"
        elif self.player.score_value < 21 or self.player.score_value > 21:
            return "Better Luck Next Time!"
