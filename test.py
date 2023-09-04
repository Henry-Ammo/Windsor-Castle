import unittest
from app import determine_prize  

class TestDeterminePrize(unittest.TestCase):

    def test_wooden_rabbit(self):
        self.assertEqual(determine_prize(25), "Congratulations! You won a wooden rabbit")

    def test_no_prize(self):
        self.assertEqual(determine_prize(100), "Oh dear, you won no prize")

    def test_wafer_thin_mint(self):
        self.assertEqual(determine_prize(175), "Congratulations! You won a wafer-thin mint")

    def test_penguin(self):
        self.assertEqual(determine_prize(190), "Congratulations! You won a penguin")

    def test_no_prize_this_time(self):
        self.assertEqual(determine_prize(201), "Oh dear, no prize this time")

if __name__ == '__main__':
    unittest.main()
