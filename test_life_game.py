# -*- coding:utf8 -*-
import unittest
import life_game as lg

lg.pygame.world = lg.np.zeros((lg.HEIGHT, lg.WIDTH))

'''分别测试了当一个活着的细胞或死去的细胞周围有n个活着细胞的时候 细胞的变化情况'''


class TestLifeGame(unittest.TestCase):
    def test_coreLogic_cell_f1_0(self):
        nbr_input_f1 = lg.np.mat([[-1 for i in range(80)] for i in range(40)])
        nbr_input_9 = lg.np.mat([[9 for i in range(80)] for i in range(40)])

        try:
            self.assertRaises(Exception, lg.judge_cell_state_exception(nbr_input_f1), -1)
            self.assertRaises(Exception, lg.judge_cell_state_exception(nbr_input_9), -1)

        except Exception as e:
            pass

    def test_coreLogic_cell_f1_1(self):
        lg.pygame.world = lg.np.ones((lg.HEIGHT, lg.WIDTH))
        self.assertEqual(lg.judge_cell_state(-1)[0][0], 0)

    def test_coreLogic_cell0_0(self):
        self.assertEqual(lg.judge_cell_state(0)[0][0], 0)

    def test_coreLogic_cell0_1(self):
        # nbr_input_0 = lg.np.mat([[0 for i in range(80)] for i in range(40)])
        lg.pygame.world = lg.np.ones((lg.HEIGHT, lg.WIDTH))
        self.assertEqual(lg.judge_cell_state(1)[0][0], 0)

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

    def test_coreLogic_cell8_0(self):
        self.assertEqual(lg.judge_cell_state(8)[0][0], 0)

    def test_coreLogic_cell8_1(self):
        lg.pygame.world = lg.np.ones((lg.HEIGHT, lg.WIDTH))
        self.assertEqual(lg.judge_cell_state(8)[0][0], 0)
