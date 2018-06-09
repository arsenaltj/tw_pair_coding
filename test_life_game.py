import unittest
import life_game as lg

lg.pygame.world = lg.np.zeros(40,80)
lg.change_state()

class TestLifeGame(unittest.TestCase):
    def test_coreLogic(self):
        self.assertEqual("123", "123")
    def test_upper2(self):
        self.assertEqual("1223", "123")