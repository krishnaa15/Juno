from juno.card import Card
from juno.deck import Deck
from juno.gameround import GameRound
from juno.hand import Hand
from juno.player import Player

print("Welcome to JUNO!")

name1= input("Player1, please enter your name: ")
name2= input("Player2, please enter your name: ")
name3= input("Player3, please enter your name: ")
name4= input("Player4, please enter your name: ")

print("\n")

c1=0
c2=0
c3=0 
c4=0
    
score1=int(c1)
score2=int(c2)
score3=int(c3)
score4=int(c4)   

choice=1
while choice != '0':
    deck=Deck()
    cards=Card.create_standard_52_cards()
    deck.add_cards(cards)
    
    hand1= Hand()
    hand2= Hand()
    hand3= Hand()
    hand4= Hand()
    
    player1=Player(name=name1, hand=hand1)
    player2=Player(name=name2, hand=hand2)
    player3=Player(name=name3, hand=hand3)
    player4=Player(name=name4, hand=hand4)
    players=[player1, player2, player3, player4]
    
    game_round=GameRound(deck=deck, players=players)
    game_round.play() 
    
    for player in players:
        print(f"{player.name} your cards are: {player.hand}.\n")
        
    for player in players: 
        index, hand_name, hand_cards = player.best_hand()
        hand_cards_strings = [str(card) for card in hand_cards]
        hand_cards_string = " and ".join(hand_cards_strings)
        print(f"{player.name} has a {hand_name} with a {hand_cards_string}.")
    
    winning_player = max(players)
    if(winning_player==player1):
        score1=score1+1
    elif(winning_player==player2):
        score2=score2+1
    elif(winning_player==player3):
        score3=score3+1
    elif(winning_player==player4):
        score4=score4+1
        
    print(f"\nThe winner is {winning_player.name}!")
    print("The scores are: ")
    print(f"{player1.name}: {score1}")
    print(f"{player2.name}: {score2}")
    print(f"{player3.name}: {score3}")
    print(f"{player4.name}: {score4}")
  
    scores=[score1,score2,score3,score4]
    choice=input("Press 1 if all players want to continue playing, else press 0 to quit: ")

print("\nThe final scores are: ")
print(f"{player1.name}: {score1}")
print(f"{player2.name}: {score2}")
print(f"{player3.name}: {score3}")
print(f"{player4.name}: {score4}\n")

if score1==max(scores):
    print(f"{player1.name} is the winner with score {score1}")
elif score2==max(scores):
    print(f"{player2.name} is the winner with score {score2}")
elif score3==max(scores):
    print(f"{player3.name} is the winner with score {score3}")
elif score4==max(scores):
    print(f"{player4.name} is the winner with score {score4}")

print("\nTHANKS FOR PLAYING!!")
