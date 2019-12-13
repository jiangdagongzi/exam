class Solution(object):
    def __init__(self):
        self.primary = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        i = 0
        j = 0
        stack = []
        pos_stack = []
        while (i < 9):
            while (j < 9):
                if board[i][j] == '.':
                    list = self.get_rest(board, i, j)
                    stack.append(list)
                    pos_stack.append((i, j))
                try:
                    board[i][j] = list.pop(0)
                except:
                    pos = self.roll_back(board, stack, pos_stack)
                    i = pos[0]
                    j = pos[1]
                self.print_board(board)
                j += 1
            i += 1
            j = 0

    def fit_in_col(self, board, i):
        list = []
        for char in board[i]:
            list.append(char)
        return [item for item in self.primary if item not in list]

    def fit_in_row(self, board, j):
        list = []
        row = [item[j] for item in board]
        for char in row:
            list.append(char)
        return [item1 for item1 in self.primary if item1 not in list]

    def fit_in_grid(self, board, i, j):
        list = []
        if i % 3 == 0:
            if j % 3 == 0:
                list.append(board[i + 1][j + 1])
                list.append(board[i + 1][j + 2])
                list.append(board[i + 2][j + 1])
                list.append(board[i + 2][j + 2])
            elif j % 3 == 1:
                list.append(board[i + 1][j - 1])
                list.append(board[i + 1][j + 1])
                list.append(board[i + 2][j - 1])
                list.append(board[i + 2][j + 1])
            elif j % 3 == 2:
                list.append(board[i + 1][j - 1])
                list.append(board[i + 1][j - 2])
                list.append(board[i + 2][j - 1])
                list.append(board[i + 2][j - 2])
        elif i % 3 == 1:
            if j % 3 == 0:
                list.append(board[i - 1][j + 1])
                list.append(board[i - 1][j + 2])
                list.append(board[i + 1][j + 1])
                list.append(board[i + 1][j + 2])
            elif j % 3 == 1:
                list.append(board[i - 1][j - 1])
                list.append(board[i - 1][j + 1])
                list.append(board[i + 1][j - 1])
                list.append(board[i + 1][j + 1])
            elif j % 3 == 2:
                list.append(board[i - 1][j - 1])
                list.append(board[i - 1][j - 2])
                list.append(board[i + 1][j - 1])
                list.append(board[i + 1][j - 2])
        elif i % 3 == 2:
            if j % 3 == 0:
                list.append(board[i - 1][j + 1])
                list.append(board[i - 1][j + 2])
                list.append(board[i - 2][j + 1])
                list.append(board[i - 2][j + 2])
            elif j % 3 == 1:
                list.append(board[i - 1][j - 1])
                list.append(board[i - 1][j + 1])
                list.append(board[i - 2][j - 1])
                list.append(board[i - 2][j + 1])
            elif j % 3 == 2:
                list.append(board[i - 1][j - 1])
                list.append(board[i - 1][j - 2])
                list.append(board[i - 2][j - 1])
                list.append(board[i - 2][j - 2])
        return [item for item in self.primary if item not in list]

    def get_rest(self, board, i, j):
        rest_in_col = self.fit_in_col(board, i)
        rest_in_row = self.fit_in_row(board, j)
        rest_in_grid = self.fit_in_grid(board, i, j)
        temp = [item for item in rest_in_col if item in rest_in_row]
        return [item1 for item1 in temp if item1 in rest_in_grid]

    def roll_back(self, board, stack, pos_stack):
        list = stack.pop(-1)
        pos = pos_stack.pop(-1)
        if len(list) != 0:
            stack.append(list)
            pos_stack.append(pos)
            board[pos[0]][pos[1]] = list.pop(0)
            return pos
        else:
            board[pos[0]][pos[1]] = '.'
            return self.roll_back(board, stack, pos_stack)

    def print_board(self, board):
        for row in board:
            print(row)
        print("###################################################################")


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
["6", ".", ".", "1", "9", "5", ".", ".", "."],
[".", "9", "8", ".", ".", ".", ".", "6", "."],
["8", ".", ".", ".", "6", ".", ".", ".", "3"],
["4", ".", ".", "8", ".", "3", ".", ".", "1"],
["7", ".", ".", ".", "2", ".", ".", ".", "6"],
[".", "6", ".", ".", ".", ".", "2", "8", "."],
[".", ".", ".", "4", "1", "9", ".", ".", "5"],
[".", ".", ".", ".", "8", ".", ".", "7", "9"]]
su = Solution()
su.solveSudoku(board)