import unittest
import snake_ladder as game
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestDiceRoll(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_roll_dice(self):
        # this test case will always pass
        throw = game.roll_dice()
        self.assertTrue(1 <= throw <= 6)
    
    @patch('random.randint', return_value=3)
    def test_roll_dice_random(self, mocked_randint):
        # this test should always pass, mocking die roll as 3
        result = game.roll_dice()
        mocked_randint.assert_called_with(1, 6)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()