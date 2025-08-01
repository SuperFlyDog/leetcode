from collections import deque

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
 
        dp[0] = True
        wordSet = set(wordDict)
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # 已经找到一个可拆分的方式，可以提前结束内部循环
        return dp[len(s)]