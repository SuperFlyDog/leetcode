class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = []
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            dp.append([])
            for col in range(n):
                dp[row].append(0)
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[0][0] = grid[0][0]
                elif i==0:
                    dp[0][j] = dp[0][j-1] + grid[0][j]
                elif j==0:
                    dp[i][0] = dp[i-1][0] + grid[i][0]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]