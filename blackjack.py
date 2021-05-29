
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

def calc_score(hand):
    score = 0
    aces = 0
    for i in range(len(hand)):
        if type(hand[i][1]) == int:
            score += hand[i][1]
        elif hand[i][1] != "Ace":
            score += 10
        else:
            aces += 1
    if aces != 0:
        for i in range(aces):
            if score <= 10:
                score += 11
            else:
                score += 1    
    return(score)      


deck = make_deck(suits, nums)
dealer_hand = deal_hand(deck)
player_hand = deal_hand(deck)
print("Dealer showing: ",dealer_hand[1])
print("Your hand: ", player_hand)
print(calc_score(player_hand))

