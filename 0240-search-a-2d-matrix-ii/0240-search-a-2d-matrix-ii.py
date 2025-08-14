class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        def binarySearch(row, col):
            # 越界检查
            if row < 0 or row >= m or col < 0 or col >= n:
                return False

            curVal = matrix[row][col]
            if curVal == target:
                return True
            elif curVal > target:
                return binarySearch(row - 1, col)  # 上移
            else:
                return binarySearch(row, col + 1)  # 右移

        # 如果 target 超出矩阵整体范围
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False

        # 从左下角开始
        return binarySearch(m - 1, 0)
