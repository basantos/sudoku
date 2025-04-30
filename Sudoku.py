# 1: Create board display DONE
# 2: Randomly generate solution DONE
# 3: Remove cells DONE
# 4: Player mechanics (insert number, remove number) DONE
# 5: Check if valid when board is complete DONE
# 6: Create difficulty levels
# 7: Create option to give up and show solution
import copy
import random


class Sudoku:
    """
    Creates an instance of a Sudoku game.
    """
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
        self._status = "In Progress"  # others: "Lost", "Won"

    def get_solution(self):
        """
        Returns puzzle's solution
        """
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
        """
        Displays each row of the board to the console.
        :param item: array
        """
        for i in range(13):
            print(item[i])

    def show_board(self):
        """
        Displays board to console.
        """
        self.display(self._board)

    def show_puzzle(self):  # for testing only
        """
        Shows puzzle to console.
        :return:
        """
        return self.display(self._puzzle)

    def show_solution(self):
        """
        Shows solution to console.
        :return:
        """
        return self._solution

    def check_row(self, board, val, row_index):
        """
        Checks if the val is already in the specified row
        """
        row = board[row_index]
        for i in [2,3,4,6,7,8,10,11,12]:
            if row[i] == val:
                return True
        return False

    def check_col(self, board, val, col_index):
        """
        Checks if val is already in the specified column
        """
        for i in [2,3,4,6,7,8,10,11,12]:
            if board[i][col_index] == val:
                return True
        return False

    def check_quad(self, board, val, row_index, col_index):
        """Checks if val is in the specified quadrant"""
        if row_index in [2,3,4]:
            row_indices = [2,3,4]
        elif row_index in [6,7,8]:
            row_indices = [6,7,8]
        else:
            row_indices = [10,11,12]

        if col_index in [2, 3, 4]:
            col_indices = [2, 3, 4]
        elif col_index in [6, 7, 8]:
            col_indices = [6, 7, 8]
        else:
            col_indices = [10, 11, 12]

        for row in row_indices:
            for col in col_indices:
                if board[row][col] == val:
                    return True
        return False

    def create_solution(self):
        """
        Creates solution for a game board.
        """
        solution = copy.deepcopy(self._board)

        choices = [1,2,3,4,5,6,7,8,9]
        # First row
        row = solution[2]
        for i in range(2,13):
            if row[i] == '_':
                num = random.choice(choices)
                choices.remove(num)
                row[i] = str(num)
         # the rest
        for j in [3,4,6,7,8,10,11,12]:
            choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            row = solution[j]
            for i in range(2,13):
                if row[i] == '_':
                    num = random.choice(choices)
                    while self.check_row(solution, num,j) and self.check_col(solution, num,i) and self.check_quad(solution, num,j,i):
                        num = random.choice(choices)
                    choices.remove(num)
                    row[i] = str(num)
        return solution

    def create_puzzle(self):
        """
        Adds some numbers from solution to board, creating the puzzle.
        """
        indices = [2, 3, 4, 6, 7, 8, 10, 11, 12]
        for i in range(18):  # 18 arbitrary; for testing purposes; will adjust by difficulty later
            row = random.choice(indices)
            col = random.choice(indices)
            self._board[row][col] = self._solution[row][col]
        return copy.deepcopy(self._board)

    def reset_puzzle(self):
        """Returns board to beginning of the puzzle state without player moves."""
        self._board = self._puzzle

    def check_solution(self):
        """Checks to see if the player solution is correct and ends the game."""
        if self._board == self._solution:
            self._status = 'WON'
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
        if self.check_row(self._board, value, row) is False and self.check_col(self._board, value, col) is False and self.check_quad(self._board, value,row,col) is False:
            if self._puzzle[row][col] == '_':
                self._board[row][col] = value
                self._num_empty_cells += 1
                self.show_board()
            else:
                print('Error: Cannot override numbers from the start of the puzzle. Please try again.')
        else:
            print("Invalid move. Please try again.")

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

    def play(self):
        while self._num_empty_cells != 0 or self._status == "In Progress":
            val = input("Please enter number: ")
            pos = input("Please enter position you want to place number: ")
            self.make_move(pos, val)


# Test area
def main():
    b = Sudoku()
    print(b.show_board())
    b.play()

if __name__ == '__main__':
    main()

