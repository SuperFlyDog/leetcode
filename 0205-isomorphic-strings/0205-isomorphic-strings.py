class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        chDict = {}
        for i in range(len(s)):
            if s[i] not in chDict:
                chDict[s[i]] = t[i]
            elif chDict[s[i]] == t[i]:
                continue
            elif chDict[s[i]] != t[i]:
                return False
        values = chDict.values()             # 取出所有 value
        if len(values) != len(set(values)):
            return False
        else:
            return True