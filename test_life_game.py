import unittest
import life_game as lg

lg.pygame.world = lg.np.zeros((lg.HEIGHT, lg.WIDTH))


class TestLifeGame(unittest.TestCase):
    def test_coreLogic_cell0_0(self):
        self.assertEqual(lg.judge_cell_state(0)[0][0], 0)

    def test_coreLogic_cell0_1(self):
        lg.pygame.world = lg.np.ones((lg.HEIGHT, lg.WIDTH))
        self.assertEqual(lg.judge_cell_state(0)[0][0], 0)

    def test_coreLogic_cell1_0(self):
        self.assertEqual(lg.judge_cell_state(1)[0][0], 0)

    def test_coreLogic_cell1_1(self):
        lg.pygame.world = lg.np.ones((lg.HEIGHT, lg.WIDTH))
        self.assertEqual(lg.judge_cell_state(0)[0][0], 0)

    def test_coreLogic_cell2_0(self):
        self.assertEqual(lg.judge_cell_state(2)[0][0], 0)

    def test_coreLogic_cell2_1(self):
        lg.pygame.world = lg.np.ones((lg.HEIGHT, lg.WIDTH))
        self.assertEqual(lg.judge_cell_state(2)[0][0], 1)

    def test_coreLogic_cell3_0(self):
        self.assertEqual(lg.judge_cell_state(3)[0][0], 1)

    def test_coreLogic_cell3_1(self):
        lg.pygame.world = lg.np.ones((lg.HEIGHT, lg.WIDTH))
        self.assertEqual(lg.judge_cell_state(3)[0][0], 1)

    def test_coreLogic_cell4_0(self):
        self.assertEqual(lg.judge_cell_state(4)[0][0], 0)

    def test_coreLogic_cell4_1(self):
        lg.pygame.world = lg.np.ones((lg.HEIGHT, lg.WIDTH))
        self.assertEqual(lg.judge_cell_state(4)[0][0], 0)

    def test_coreLogic_cell8_0(self):
        self.assertEqual(lg.judge_cell_state(8)[0][0], 0)

    def test_coreLogic_cell8_1(self):
        lg.pygame.world = lg.np.ones((lg.HEIGHT, lg.WIDTH))
        self.assertEqual(lg.judge_cell_state(8)[0][0], 0)
