import copy
import unittest
import Sudoku


class Test(unittest.TestCase):
    def test_check_solution_pass(self):
        b = Sudoku.Sudoku()
        solution = copy.deepcopy(b.get_solution())
        b.set_board()
        self.assertEqual(b.check_solution(), solution)
        b.make_move('a1', 5)

    def test_check_solution_not_pass(self):
        b = Sudoku.Sudoku()
        solution = copy.deepcopy(b.get_solution())
        b.set_board()
        b.make_move('a1', 10)
        self.assertNotEqual(b.check_solution(), solution)
