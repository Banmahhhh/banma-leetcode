# soooooooooo brilliant
# need to learn each line implementation
# how can you write code like this!!!!!
# don't understand the last line
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return 
        row, col = len(board), len(board[0])
        if row >= col:
            origin_o = [ij for k in range(row) for ij in ((0,k), (k, 0), (k, col-1), (row-1, k))]
        else:
            origin_o = [ij for k in range(col) for ij in ((0,k), (k, 0), (k, col-1), (row-1, k))]
        while origin_o:
            i, j = origin_o.pop()
            if 0<=i<row and 0<=j<col and board[i][j] == 'O':
                board[i][j] = 'S'
                origin_o += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        for row in board:
            for j, ele in enumerate(row):
                row[j] = 'XO' [ele == 'S']
