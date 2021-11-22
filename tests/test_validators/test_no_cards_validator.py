import unittest 

from juno.card import Card
from juno.validators import NoCardsValidator

class NoCardsValidatorTest(unittest.TestCase):
    def test_validates_no_cards(self):
        validator=NoCardsValidator(cards=[])
        
        self.assertEqual(
            validator.is_valid(),
            True
            )
    def test_returns_no_valid_cards(self):
        validator=NoCardsValidator(cards=[])
        self.assertEqual(validator.valid_cards(), [])