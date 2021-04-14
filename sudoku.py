
class Sudoku_Solver:

    board = []

    def __init__(self):
        self.board = self.initialize_board()

    def initialize_board(self):
        gameBoard = []
        for _ in range(9):
            row = []
            for _ in range(9):
                row.append(0)
            gameBoard.append(row)
        return gameBoard

    def row_checker(self, num, row):
        return not num in self.board[row]

    def col_checker(self, num, col):
        cols = []
        for i in range(len(self.board)):
            cols.append(self.board[i][col])
        return not num in cols

    def box_checker(self, num, col, row):
        (t_r_coord, t_c_coord) = self.find_top_left_coord(row, col)
        box_list = []
        for i in range(t_r_coord, t_r_coord + 3):
            for j in range(t_c_coord, t_c_coord + 3):
                box_list.append(self.board[i][j])
        return not num in box_list

    def find_top_left_coord(self, row, col):
        off_row = row % 3
        off_col = col % 3
        return(row - off_row, col-off_col)

    def is_valid(self, num, row, col):
        return self.row_checker(num, row) and self.col_checker(num, col) and self.box_checker(num, col, row)

    def solve_board(self):
        board_size = range(len(self.board))
        for row in board_size:
            for col in board_size:
                if self.board[row][col] == 0:
                    for i in board_size:
                        if self.is_valid(i+1, row, col):
                            self.board[row][col] = i + 1
                            if self.solve_board():
                                return True
                            else:
                                self.board[row][col] = 0
                    return False
        return True


solver = Sudoku_Solver()
solver.solve_board()
for i in solver.board:
    print(i)
