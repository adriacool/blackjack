
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

def hit_me(hand):
    hand.append(deck.pop(randint(0, len(deck)-1)))
    return hand    

def dealer_play(hand):
    score = calc_score(hand)
    while score < 17:
        hand = hit_me(hand)
        score = calc_score(hand)
    print("Dealer's hand:", hand)    
    return(hand)  

def player_play(hand):
    play = ' '
    while (play.lower() != 'h') and (play.lower() != 's'):
        play = input("Type S for stay. Type H for hit me. ")
    else: 
        if (play.lower() == 'h'):
            hand = hit_me(hand)
        print("Your hand:", hand)  
    return(hand, play.lower())    

deck = make_deck(suits, nums)
dealer_hand = deal_hand(deck)
player_hand = deal_hand(deck)
print("Dealer showing: ",dealer_hand[1])
print("Your hand: ", player_hand)
choice = ' '      
while (calc_score(player_hand) < 21) and (choice != 's'):
    choice = player_play(player_hand)[1]  
player_score = calc_score(player_hand)
if player_score > 21:
    print(player_score, 'BUST')
else:
    print(player_score)
    dealer_play(dealer_hand)
    dealer_score = calc_score(dealer_hand)
    if dealer_score > 21:
        print(dealer_score, "Dealer BUSTS. You WIN!")
    elif dealer_score >= player_score:
        print(dealer_score, "Dealer Wins!")
    else:
        print(dealer_score,"\nYou WIN!")

