class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        m = len(s)
        n = len(t)
        if not s and t:
            return True
        
        elif s and t:
            while j < n:
                chs = s[i]
                cht = t[j]
                if chs == cht:
                    i += 1
                if i == m:
                    return True
                j += 1
        return False
        
