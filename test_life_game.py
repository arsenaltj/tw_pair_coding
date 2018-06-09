import unittest
import life_game

class TestLifeGame(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("123", "123")
    def test_upper2(self):
        self.assertEqual("1223", "123")