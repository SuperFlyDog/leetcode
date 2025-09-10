class Solution(object):
    def getOnes(self,board,i,j):
        OneCount = 0
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and not (x == i and y == j):
                    OneCount += board[x][y]

        return OneCount
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        nboard = [row[:] for row in board]
        for i in range(m):
            for j in range(n):
                live = self.getOnes(board,i,j)
                if board[i][j] == 1 and live < 2:
                    nboard[i][j] = 0
                elif board[i][j] == 1 and (live == 2 or live == 3):
                    nboard[i][j] = 1
                elif board[i][j] == 1 and live > 3:
                    nboard[i][j] = 0
                elif board[i][j] == 0 and live == 3:
                    nboard[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = nboard[i][j]
