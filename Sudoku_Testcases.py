import copy
import unittest
import Sudoku


class Test(unittest.TestCase):
    def test_check_solution(self):
        b = Sudoku.Sudoku()
        solution = copy.deepcopy(b.get_solution())
        b.set_board()
        self.assertEqual(b.check_solution(), solution)
