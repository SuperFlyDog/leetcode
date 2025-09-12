class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        if len(pattern) != len(s):
            return False
        chDict = {}
        for i in range(len(pattern)):
            if pattern[i] not in chDict:
                chDict[pattern[i]] = s[i]
            elif chDict[pattern[i]] == s[i]:
                continue
            elif chDict[pattern[i]] != s[i]:
                return False
        values = chDict.values()             # 取出所有 value
        if len(values) != len(set(values)):
            return False
        else:
            return True