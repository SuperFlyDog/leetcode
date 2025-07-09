class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        print(squares)
        for i in range(1, n+1):
            for square in squares:
                if i >= square:
                    dp[i] = min(dp[i], dp[i-square] + 1)

        return dp[n]