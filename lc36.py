'''
check by row/ column/ sub-box of grid
use set to remove duplicate
'''
class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        answer = False
        for i in range(9):
            a = [x for x in board[i] if x != '.']
            if len(a) != len(set(a)):
                return False
        for i in range(9):
            a = []
            for j in range(9):
                if board[j][i] != '.':
                    a.append(board[j][i])
            if len(a) != len(set(a)):
                return False
        for i in range(9):
            a = []
            for j in range(9):
                x = 3*int(i/3)+int(j/3)
                y = 3*(i%3)+j%3
                if board[x][y] != '.':
                    a.append(board[x][y])
            if len(a) != len(set(a)):
                return False
        return True