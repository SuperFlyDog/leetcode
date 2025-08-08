class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row0 = []
        col0 = []
        
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row0.append(i)
                    col0.append(j)
        print(row0)
        print(col0)
        for x in row0:
            for j in range(col):
                matrix[x][j] = 0

        for row1 in range(row): 
            for y in col0:
                matrix[row1][y] = 0