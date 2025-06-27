class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        dia1 = set()
        dia2 = set()
        cols = set() 
        res = []
        curDB = [['.'] * n for _ in range(n)]
        def backtrack(row):
            
            if row == n:
                # 收集解
                res.append([''.join(r) for r in curDB])
                return
            for col in range(n):
                if (col not in cols and 
                    (row - col) not in dia1 and 
                    (row + col) not in dia2):
                    # 做选择
                    cols.add(col)
                    dia1.add(row - col)
                    dia2.add(col + row)

                    curDB[row][col] = 'Q'
                    backtrack(row + 1)
                    # 撤销选择
                    cols.remove(col)
                    dia1.remove(row - col)
                    dia2.remove(row + col)
                    curDB[row][col] = '.'

        backtrack(0)
        return res