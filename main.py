from juno.card import Card
from juno.deck import Deck
from juno.gameround import GameRound
from juno.hand import Hand
from juno.player import Player

deck=Deck()
cards=Card.create_standard_52_cards()
deck.add_cards(cards)

hand1= Hand()
hand2= Hand()
hand3= Hand()
hand4= Hand()

print("Welcome to JUNO!")

name1= input("Player1, please enter your name: ")
name2= input("Player2, please enter your name: ")
name3= input("Player3, please enter your name: ")
name4= input("Player4, please enter your name: ")

print("\n")

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

print(f"\nThe winner is {winning_player.name}!")
print("\nThanks for playing")