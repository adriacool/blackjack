
from random import randint

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
nums = [2,3,4,5,6,7,8,9,10, "Jack", "Queen", "King", "Ace"]

def make_deck(suits, nums):
        deck = []
        for suit in suits:
            for num in nums:
                deck.append((suit,num))
        return deck

def deal_hand(deck):
    hand = []
    for i in range(2):
      hand.append(deck.pop(randint(0, len(deck)-1)))
    return hand


deck = make_deck(suits, nums)
dealer_hand = deal_hand(deck)
player_hand = deal_hand(deck)
print("Dealer showing: ",dealer_hand[1])
print("Your hand: ", player_hand)


