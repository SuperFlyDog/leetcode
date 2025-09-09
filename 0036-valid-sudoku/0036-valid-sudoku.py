class Solution(object):
    def rowValid(self,board,row):
        seen = set()
        for cell in board[row]:
            if cell == '.':
                continue
            else:
                if cell in seen:
                    return False
                else:
                    seen.add(cell)
        return True

    def colValid(self,board,col):
        seen = set()
        colArr = []
        for rowArr in board:
            colArr.append(rowArr[col])
        for cell in colArr:
            if cell == '.':
                continue
            else:
                if cell in seen:
                    return False
                else:
                    seen.add(cell)
        return True

    def boxValid(self,board,box):
        seen = set()
        boxArr = []
        cenRow = (box // 3) * 3 + 1
        cenCol = (box % 3) * 3 + 1
        for i in range(cenRow-1,cenRow+2):
            for j in range(cenCol-1,cenCol+2):
                boxArr.append(board[i][j])

        for cell in boxArr:
            if cell == '.':
                continue
            else:
                if cell in seen:
                    return False
                else:
                    seen.add(cell)
        return True    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for num in range(9):
            if self.rowValid(board,num) and self.colValid(board,num) and self.boxValid(board,num):
                continue
            else:
                return False
        return True