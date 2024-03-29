class Player():
    def __init__(self, name,hand):
        self.name=name
        self.hand=hand
        
    def __gt__(self, other):
        current_player_best_validator=self.best_hand()[0]
        other_player_best_validator=other.best_hand()[0]
        return current_player_best_validator < other_player_best_validator
        
    def best_hand(self):
        return self.hand.best_rank()
    
    def add_cards(self, cards):
        self.hand.add_cards(cards)
        
    def wants_to_fold(self):
        return False
        
    