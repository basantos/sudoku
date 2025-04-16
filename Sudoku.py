# 1: Create board display DONE
# 2: Randomly generate solution Later
# 3: Remove cells DONE
# 4: Player mechanics (insert number, remove number)
# 5: Check if valid when board is complete
import copy
import random


class Sudoku:
    def __init__(self):
        self._board = [['_', '|', 'a', 'b', 'c', '|', 'd', 'e', 'f', '|', 'g', 'h', 'i'],
                       ['-------------------------------------------------------------'],
                       ['1', '|', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_'],
                       ['2', '|', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_'],
                       ['3', '|', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_'],
                       ['-------------------------------------------------------------'],
                       ['4', '|', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_'],
                       ['5', '|', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_'],
                       ['6', '|', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_'],
                       ['-------------------------------------------------------------'],
                       ['7', '|', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_'],
                       ['8', '|', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_'],
                       ['9', '|', '_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_']]
        self._solution = self.create_solution()
        self._puzzle = self.create_puzzle()
        self._num_empty_cells = 63  # since each puzzle has 18 cells filled initially, 63 is left

    def get_solution(self):
        return self._solution

    def set_board(self):
        """For testing only"""
        self._board = [['_', '|', 'a', 'b', 'c', '|', 'd', 'e', 'f', '|', 'g', 'h', 'i'],
                ['-------------------------------------------------------------'],
                ['1', '|', '1', '2', '3', '|', '4', '5', '6', '|', '7', '8', '9'],
                ['2', '|', '4', '5', '6', '|', '7', '8', '9', '|', '1', '2', '3'],
                ['3', '|', '7', '8', '9', '|', '1', '2', '3', '|', '4', '5', '6'],
                ['-------------------------------------------------------------'],
                ['4', '|', '2', '6', '1', '|', '5', '3', '4', '|', '9', '7', '8'],
                ['5', '|', '3', '7', '4', '|', '2', '9', '8', '|', '6', '1', '5'],
                ['6', '|', '5', '9', '8', '|', '6', '1', '7', '|', '2', '3', '4'],
                ['-------------------------------------------------------------'],
                ['7', '|', '6', '1', '2', '|', '8', '4', '5', '|', '3', '9', '7'],
                ['8', '|', '8', '3', '5', '|', '9', '7', '1', '|', '4', '6', '2'],
                ['9', '|', '9', '4', '7', '|', '3', '6', '2', '|', '8', '5', '1']]

    def display(self, item):
        for i in range(13):
            print(item[i])

    def show_board(self):
        self.display(self._board)

    def show_puzzle(self):  # for testing only
        return self.display(self._puzzle)

    def create_solution(self):
        """
        Creates solution for a game board.
        """
        # Do Later
        # choices = [1,2,3,4,5,6,7,8,9]
        # # First row
        # row = self._board[2]
        # for i in range(2,13):
        #     if row[i] == '_':
        #         num = random.choice(choices)
        #         choices.remove(num)
        #         row[i] = str(num)

        # for testing only
        return [['_', '|', 'a', 'b', 'c', '|', 'd', 'e', 'f', '|', 'g', 'h', 'i'],
                ['-------------------------------------------------------------'],
                ['1', '|', '1', '2', '3', '|', '4', '5', '6', '|', '7', '8', '9'],
                ['2', '|', '4', '5', '6', '|', '7', '8', '9', '|', '1', '2', '3'],
                ['3', '|', '7', '8', '9', '|', '1', '2', '3', '|', '4', '5', '6'],
                ['-------------------------------------------------------------'],
                ['4', '|', '2', '6', '1', '|', '5', '3', '4', '|', '9', '7', '8'],
                ['5', '|', '3', '7', '4', '|', '2', '9', '8', '|', '6', '1', '5'],
                ['6', '|', '5', '9', '8', '|', '6', '1', '7', '|', '2', '3', '4'],
                ['-------------------------------------------------------------'],
                ['7', '|', '6', '1', '2', '|', '8', '4', '5', '|', '3', '9', '7'],
                ['8', '|', '8', '3', '5', '|', '9', '7', '1', '|', '4', '6', '2'],
                ['9', '|', '9', '4', '7', '|', '3', '6', '2', '|', '8', '5', '1']]

    def create_puzzle(self):
        """
        Adds some numbers from solution to board.
        """
        indices = [2, 3, 4, 6, 7, 8, 10, 11, 12]
        for i in range(18):  # 18 arbitrary; for testing purposes; will adjust by difficulty later
            row = random.choice(indices)
            col = random.choice(indices)
            self._board[row][col] = self._solution[row][col]
        return copy.deepcopy(self._board)

    def reset_puzzle(self):
        self._board = self._puzzle

    def check_solution(self):
        if self._board == self._solution:
            print('Congratulations! You won!')
        else:
            print('Sorry, please check your solution and try again.')
        return self._board

    def make_move(self, position, value):
        """
        Adds value to the position on the board and displays board.
        Overwrites previous moves, but not numbers present at start of puzzle.
        :param position: string
        :param value: string
        :return: None
        """
        position_list = list(position)
        row = position_list[1]
        i = 0
        while type(row) is str:
            if self._board[i][0] == row:
                row = i
            i += 1
        col = self._board[0].index(position_list[0])

        # Only write value on positions that were blanks at the beginning of the puzzle
        if self._puzzle[row][col] == '_':
            self._board[row][col] = value
            self._num_empty_cells += 1
            self.show_board()
        else:
            print('Error: Cannot override numbers from the start of the puzzle. Please try again.')

        if self._num_empty_cells == 0:
            self.check_solution()


    def erase(self, position):
        position_list = list(position)
        row = position_list[1]
        i = 0
        while type(row) is str:
            if self._board[i][0] == row:
                row = i
            i += 1
        col = self._board[0].index(position_list[0])

        # Only erases value on positions that were blanks at the beginning of the puzzle
        if self._puzzle[row][col] == '_':
            self._board[row][col] = '_'
            self.show_board()
            self._num_empty_cells -= 1
        else:
            print('Error: Cannot override numbers from the start of the puzzle. Please try again.')

        if self._num_empty_cells == 0:
            self.check_solution()


# Test area
b = Sudoku()
# print(b.show_board())
# print(b.make_move('b1', '2'))
# print(b.show_puzzle())  # makes sure original puzzle not changed
b.check_solution()
