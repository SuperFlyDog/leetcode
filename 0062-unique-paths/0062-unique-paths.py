class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = []
        for row in range(m):
            dp.append([])
            for col in range(n):
                dp[row].append(0)
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
