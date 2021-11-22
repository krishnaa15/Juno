import unittest
from unittest.mock import MagicMock,call

from juno.gameround import GameRound
from juno.card import Card

class GameRoundTest(unittest.TestCase):
    def setUp(self):
        self.first_2_cards=[
            Card(rank="2",suit="Hearts"),
            Card(rank="6", suit="Clubs")
            
            ]
        self.next_2_cards=[
            Card(rank="9",suit="Diamonds"),
            Card(rank="4", suit="Spades")
            ]
        self.flop_cards=[
            Card(rank="3",suit="Diamonds"),
            Card(rank="4",suit="Hearts"),
            Card(rank="10",suit="Clubs")
            ]
        self.turn_card=[Card(rank="9", suit="Spades")]
        self.river_card=[Card(rank="Queen",suit="Clubs")]
    
    def test_stores_deck_and_players(self):
        deck=MagicMock()
        players=[
            MagicMock(),
            MagicMock()
            ]
        gameround=GameRound(
            deck=deck,
            players=players
            )
        self.assertEqual(
            gameround.deck,
            deck
            )
        self.assertEqual(
            gameround.players,
            players
            )
        
    def test_shuffles_deck(self):
        mock_deck=MagicMock()
        players=[
            MagicMock(),
            MagicMock()
            ]
        gameround=GameRound(
            deck=mock_deck,
            players=players
            )
        gameround.play()
        mock_deck.shuffle.assert_called_once()
        
    def test_deals_2_cards_from_deck_to_each_player(self):
        mock_deck=MagicMock()
        mock_deck.remove_cards.side_effect=[
            self.first_2_cards,
            self.next_2_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
        ]
        
        mock_player1=MagicMock()
        mock_player2=MagicMock()
        players=[mock_player1, mock_player2]
        
        gameround=GameRound(
            deck=mock_deck,
            players=players
            )
        
        gameround.play()
        mock_deck.remove_cards.asssert_has_calls([
            call(2), call(2)
            ])
        
        mock_player1.add_cards.assert_has_calls([
            call(self.first_2_cards)
            ])   
        mock_player2.add_cards.assert_has_calls([
            call(self.next_2_cards)
            ])
        
    def test_removes_player_who_folds(self):
        deck=MagicMock()
        player1=MagicMock()
        player2=MagicMock()
        
        player1.wants_to_fold.return_value=True
        player2.wants_to_fold.return_value=False
        players=[player1,player2]
        
        gameround=GameRound(deck=deck, players=players)
        gameround.play()
        
        self.assertEqual(
            gameround.players, 
            [player2]
            )
        
    def test_deals_3flop_1turn_1river_cards(self):
        mock_player1=MagicMock()
        mock_player1.wants_to_fold.return_value=False
        mock_player2=MagicMock()
        mock_player2.wants_to_fold.return_value=False
        players=[mock_player1, mock_player2]        
        
        mock_deck=MagicMock()
        mock_deck.remove_cards.side_effect=[
            self.first_2_cards,
            self.next_2_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
            ]
        
        gameround=GameRound(deck=mock_deck, players=players)
        gameround.play()
        
        mock_deck.remove_cards.assert_has_calls([
            call(3),call(1),call(1)
             ])
        
        calls=[
            call(self.flop_cards),
            call(self.turn_card),
            call(self.river_card)
            ]
        for player in players:
            player.add_cards.assert_has_calls(calls)
        
        
